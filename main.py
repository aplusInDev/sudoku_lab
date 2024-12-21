from ui import SudokuApp
from data import default_sudoku

if __name__ == "__main__":
    app = SudokuApp(default_sudoku)
    app.root.mainloop()