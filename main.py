from ui.sudoku_app import SudokuApp
from data.default_grids import default_sudoku

if __name__ == "__main__":
    app = SudokuApp(default_sudoku)
    app.root.mainloop()