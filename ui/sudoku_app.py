import tkinter as tk
from tkinter import ttk, messagebox
from typing import List
from models.problem import Problem
from solvers.sudoku_solver import SudokuSolver

class SudokuApp:
    def __init__(self, default_grid: List[List[int]], method: str = "DFS"):
        self.root = tk.Tk()
        self.root.title("Enhanced Sudoku Solver")
        self.root.configure(bg='#f0f0f0')
        
        self.grid = [[tk.StringVar() for _ in range(9)] for _ in range(9)]
        self.default_grid = default_grid
        self.method = method
        self.solving = False
        
        self._setup_ui()
        self.load_default_grid()

    def _setup_ui(self) -> None:
        """Sets up the complete UI with enhanced styling."""
        self._create_title_frame()
        self._create_grid_frame()
        self._create_controls_frame()
        self._create_status_frame()
        self._setup_bindings()

    def _create_title_frame(self) -> None:
        """Creates the title section."""
        title_frame = ttk.Frame(self.root, padding="10")
        title_frame.pack(fill='x')
        
        title_label = ttk.Label(
            title_frame,
            text="Enhanced Sudoku Solver",
            font=('Arial', 16, 'bold')
        )
        title_label.pack()

    def _create_grid_frame(self) -> None:
        """Creates the Sudoku grid with improved styling."""
        grid_frame = ttk.Frame(self.root, padding="10")
        grid_frame.pack()

        for i in range(9):
            for j in range(9):
                cell_frame = ttk.Frame(
                    grid_frame,
                    borderwidth=1,
                    relief='solid'
                )
                cell_frame.grid(
                    row=i, column=j,
                    padx=(1 if j % 3 else 2),
                    pady=(1 if i % 3 else 2)
                )
                
                entry = ttk.Entry(
                    cell_frame,
                    textvariable=self.grid[i][j],
                    width=3,
                    justify='center',
                    font=('Arial', 14)
                )
                entry.pack(padx=1, pady=1)

    def _create_controls_frame(self) -> None:
        """Creates the control panel with solver options."""
        controls_frame = ttk.LabelFrame(self.root, text="Controls", padding="10")
        controls_frame.pack(fill='x', padx=10, pady=5)

        # Algorithm selection
        algo_frame = ttk.Frame(controls_frame)
        algo_frame.pack(fill='x', pady=5)
        
        ttk.Label(algo_frame, text="Algorithm:").pack(side='left', padx=5)
        self.method_selector = ttk.Combobox(
            algo_frame,
            values=["DFS", "BFS", "DLS"],
            state="readonly",
            width=15
        )
        self.method_selector.set(self.method)
        self.method_selector.pack(side='left', padx=5)
        
        # Buttons
        button_frame = ttk.Frame(controls_frame)
        button_frame.pack(fill='x', pady=5)
        
        self.solve_button = ttk.Button(
            button_frame,
            text="Solve",
            command=self.solve,
            style='Accent.TButton'
        )
        self.solve_button.pack(side='left', padx=5)
        
        ttk.Button(
            button_frame,
            text="Clear",
            command=self.clear_grid
        ).pack(side='left', padx=5)
        
        ttk.Button(
            button_frame,
            text="Load Default",
            command=self.load_default_grid
        ).pack(side='left', padx=5)

    def _create_status_frame(self) -> None:
        """Creates the status bar for showing solver progress."""
        self.status_frame = ttk.Frame(self.root, padding="5")
        self.status_frame.pack(fill='x', side='bottom')
        
        self.status_var = tk.StringVar(value="Ready")
        self.status_label = ttk.Label(
            self.status_frame,
            textvariable=self.status_var,
            font=('Arial', 10)
        )
        self.status_label.pack(side='left')
        
        self.progress_bar = ttk.Progressbar(
            self.status_frame,
            mode='indeterminate',
            length=200
        )
        self.progress_bar.pack(side='right', padx=5)

    def _setup_bindings(self) -> None:
        """Sets up event bindings for the UI."""
        self.method_selector.bind('<<ComboboxSelected>>', self._on_method_change)
        
        for i in range(9):
            for j in range(9):
                self.grid[i][j].trace('w', lambda *args, i=i, j=j: self._validate_input(i, j))

    def _validate_input(self, i: int, j: int) -> None:
        """Validates user input in grid cells."""
        value = self.grid[i][j].get()
        if value:
            try:
                num = int(value)
                if not (0 <= num <= 9):
                    self.grid[i][j].set('')
            except ValueError:
                self.grid[i][j].set('')

    def _on_method_change(self, event) -> None:
        """Handles algorithm selection changes."""
        self.method = self.method_selector.get()

    def load_default_grid(self) -> None:
        """Loads the default Sudoku puzzle."""
        for i in range(9):
            for j in range(9):
                self.grid[i][j].set(str(self.default_grid[i][j]) if self.default_grid[i][j] != 0 else '')

    def clear_grid(self) -> None:
        """Clears the entire grid."""
        for i in range(9):
            for j in range(9):
                self.grid[i][j].set('')

    def get_grid_values(self) -> List[List[int]]:
        """Gets the current grid values as a 2D list of integers."""
        return [[int(self.grid[i][j].get()) if self.grid[i][j].get() else 0 
                for j in range(9)] for i in range(9)]

    def display_solution(self, solution: List[List[int]]) -> None:
        """Displays the solution in the grid."""
        if not solution:
            messagebox.showwarning("No Solution", "No solution found for the given puzzle.")
            return
            
        for i in range(9):
            for j in range(9):
                self.grid[i][j].set(str(solution[i][j]))

    def solve(self) -> None:
        """Initiates the solving process."""
        if self.solving:
            return
            
        self.solving = True
        self.status_var.set(f"Solving with {self.method}...")
        self.progress_bar.start()
        self.solve_button.state(['disabled'])
        
        try:
            current_grid = self.get_grid_values()
            problem = Problem(current_grid)
            solver = SudokuSolver(problem)
            
            solution = None
            if self.method == 'DFS':
                solution = solver.dfs()
            elif self.method == 'BFS':
                solution = solver.bfs()
            elif self.method == 'DLS':
                solution = solver.dls()
                
            self.display_solution(solution)
            self.status_var.set(f"Solved with {self.method}!" if solution else "No solution found")
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.status_var.set("Error: Invalid puzzle")
            
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
            self.status_var.set("Error occurred")
            
        finally:
            self.solving = False
            self.progress_bar.stop()
            self.solve_button.state(['!disabled'])

    def run(self) -> None:
        """Starts the application."""
        self.root.mainloop()
