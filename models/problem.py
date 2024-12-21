from typing import List, Set, Tuple
import numpy as np
from collections import defaultdict

class Problem:
    def __init__(self, initial_state: List[List[int]]):
        self.initial_state = initial_state
        self.size = len(initial_state)
        self.subgrid_size = int(np.sqrt(self.size))
        self._validate_initial_state()

    def _validate_initial_state(self) -> None:
        """Validates the initial state of the Sudoku puzzle."""
        if not self.is_valid(self.initial_state):
            raise ValueError("Invalid initial Sudoku state")

    def is_goal(self, state: List[List[int]]) -> bool:
        """Checks if the current state is a complete and valid solution."""
        return all(all(cell != 0 for cell in row) for row in state) and self.is_valid(state)

    def is_valid(self, state: List[List[int]]) -> bool:
        """Checks if the current state is valid according to Sudoku rules."""
        return (self._check_rows(state) and 
                self._check_columns(state) and 
                self._check_subgrids(state))

    def _check_rows(self, state: List[List[int]]) -> bool:
        """Validates all rows in the grid."""
        return all(self._is_valid_group([state[i][j] for j in range(self.size)])
                  for i in range(self.size))

    def _check_columns(self, state: List[List[int]]) -> bool:
        """Validates all columns in the grid."""
        return all(self._is_valid_group([state[i][j] for i in range(self.size)])
                  for j in range(self.size))

    def _check_subgrids(self, state: List[List[int]]) -> bool:
        """Validates all subgrids in the grid."""
        return all(self._is_valid_group(self._get_subgrid_values(state, row, col))
                  for row in range(0, self.size, self.subgrid_size)
                  for col in range(0, self.size, self.subgrid_size))

    def _is_valid_group(self, group: List[int]) -> bool:
        """Checks if a group (row/column/subgrid) contains valid values."""
        values = [x for x in group if x != 0]
        return len(values) == len(set(values))

    def _get_subgrid_values(self, state: List[List[int]], start_row: int, start_col: int) -> List[int]:
        """Gets all values in a subgrid starting at the given position."""
        values = []
        for i in range(self.subgrid_size):
            for j in range(self.subgrid_size):
                values.append(state[start_row + i][start_col + j])
        return values

    def get_next_empty_cell(self, state: List[List[int]]) -> Tuple[int, int]:
        """Finds the next empty cell using MRV (Minimum Remaining Values) heuristic."""
        min_options = float('inf')
        min_position = (-1, -1)
        
        for i in range(self.size):
            for j in range(self.size):
                if state[i][j] == 0:
                    options = len(self._get_valid_values(state, i, j))
                    if options < min_options:
                        min_options = options
                        min_position = (i, j)
        
        return min_position

    def _get_valid_values(self, state: List[List[int]], row: int, col: int) -> Set[int]:
        """Gets all valid values for a given cell."""
        if state[row][col] != 0:
            return set()

        row_values = set(state[row])
        col_values = set(state[i][col] for i in range(self.size))
        
        subgrid_row = (row // self.subgrid_size) * self.subgrid_size
        subgrid_col = (col // self.subgrid_size) * self.subgrid_size
        subgrid_values = set(self._get_subgrid_values(state, subgrid_row, subgrid_col))
        
        used_values = row_values | col_values | subgrid_values
        return set(range(1, self.size + 1)) - used_values

    def get_successors(self, state: List[List[int]]) -> List[Tuple[List[List[int]], Tuple[int, int]]]:
        """Generates successor states using MRV and forward checking."""
        row, col = self.get_next_empty_cell(state)
        if row == -1 and col == -1:
            return []

        successors = []
        valid_values = self._get_valid_values(state, row, col)
        
        for value in valid_values:
            new_state = [row[:] for row in state]
            new_state[row][col] = value
            if self.is_valid(new_state):
                successors.append((new_state, (row, col)))
                
        return successors

    def heuristic(self, state: List[List[int]]) -> float:
        """Calculates heuristic value using a combination of empty cells and constraint satisfaction."""
        empty_cells = sum(row.count(0) for row in state)
        constraints_violated = self._count_constraint_violations(state)
        return empty_cells + (constraints_violated * 0.5)

    def _count_constraint_violations(self, state: List[List[int]]) -> int:
        """Counts the number of constraint violations in the current state."""
        violations = 0
        
        # Check rows and columns
        for i in range(self.size):
            row_counts = defaultdict(int)
            col_counts = defaultdict(int)
            for j in range(self.size):
                if state[i][j] != 0:
                    row_counts[state[i][j]] += 1
                if state[j][i] != 0:
                    col_counts[state[j][i]] += 1
            
            violations += sum(count - 1 for count in row_counts.values() if count > 1)
            violations += sum(count - 1 for count in col_counts.values() if count > 1)

        # Check subgrids
        for row in range(0, self.size, self.subgrid_size):
            for col in range(0, self.size, self.subgrid_size):
                subgrid_counts = defaultdict(int)
                for i in range(self.subgrid_size):
                    for j in range(self.subgrid_size):
                        value = state[row + i][col + j]
                        if value != 0:
                            subgrid_counts[value] += 1
                violations += sum(count - 1 for count in subgrid_counts.values() if count > 1)

        return violations
