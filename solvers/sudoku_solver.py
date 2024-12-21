import time
from typing import List, Optional
from collections import deque
from models import Node, Problem

class SudokuSolver:
    """Sudoku puzzle solver using various search algorithms."""
    method_used = ""
    def __init__(self, problem: Problem):
        self.problem = problem
        self.solution = None
        self.nodes_explored = 0
        self.max_depth_reached = 0

    def _update_statistics(self, node: Node) -> None:
        """Updates solver statistics."""
        self.nodes_explored += 1
        self.max_depth_reached = max(self.max_depth_reached, node.depth)

    def dfs(self, max_depth: Optional[int] = None) -> Optional[List[List[int]]]:
        """Depth-First Search with optional depth limit."""
        self.method_used = "DFS"
        start_time = time.time()
        self.nodes_explored = 0
        self.max_depth_reached = 0
        
        stack = [Node(self.problem.initial_state)]
        
        while stack:
            node = stack.pop()
            self._update_statistics(node)
            
            if max_depth is not None and node.depth > max_depth:
                continue
                
            if self.problem.is_goal(node.state):
                self.solution = node.state
                self._print_statistics(start_time)
                return node.state
                
            successors = self.problem.get_successors(node.state)
            for new_state, position in reversed(successors):
                child = Node(
                    state=new_state,
                    parent=node,
                    depth=node.depth + 1,
                    position=position
                )
                stack.append(child)
                
        return None

    def bfs(self) -> Optional[List[List[int]]]:
        """Breadth-First Search with optimization for memory usage."""
        self.method_used = "BFS"
        start_time = time.time()
        self.nodes_explored = 0
        self.max_depth_reached = 0
        
        queue = deque([Node(self.problem.initial_state)])
        seen_states = {str(self.problem.initial_state)}
        
        while queue:
            node = queue.popleft()
            self._update_statistics(node)
            
            if self.problem.is_goal(node.state):
                self.solution = node.state
                self._print_statistics(start_time)
                return node.state
                
            successors = self.problem.get_successors(node.state)
            for new_state, position in successors:
                state_str = str(new_state)
                if state_str not in seen_states:
                    child = Node(
                        state=new_state,
                        parent=node,
                        depth=node.depth + 1,
                        position=position
                    )
                    queue.append(child)
                    seen_states.add(state_str)
                    
        return None
    
    def dls(self, limit: Optional[int] = 50) -> Optional[List[List[int]]]:
        """Depth-Limited Search with optional depth limit."""
        self.method_used = "DLS"
        start_time = time.time()
        self.nodes_explored = 0
        self.max_depth_reached = 0
        
        stack = [Node(self.problem.initial_state)]
        
        while stack:
            node = stack.pop()
            self._update_statistics(node)
            
            if self.problem.is_goal(node.state):
                self.solution = node.state
                self._print_statistics(start_time)
                return node.state
                
            if node.depth < limit:
                successors = self.problem.get_successors(node.state)
                for new_state, position in successors:
                    child = Node(
                        state=new_state,
                        parent=node,
                        depth=node.depth + 1,
                        position=position
                    )
                    stack.append(child)
                    
        print("Aucune solution trouvée ou limite atteinte.")
        self._print_statistics(start_time)
        return None

    def _print_statistics(self, start_time: float) -> None:
        """Prints solver statistics."""
        elapsed_time = time.time() - start_time
        print(f"\nSolver Statistics:")
        print(f"Algorithm: {self.method_used}")
        print(f"Time taken: {elapsed_time:.2f} seconds")
        print(f"Nodes explored: {self.nodes_explored}")
        print(f"Maximum depth reached: {self.max_depth_reached}")
        print(f"Solution steps: {self.max_depth_reached + 1}")
