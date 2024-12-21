# Sudoku Solver Based on AI Search Algorithms

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Example](#example)
- [Contributing](#contributing)

## Description

This project is a Sudoku solver developed in Python that utilizes artificial intelligence search algorithms to solve puzzles. The program features a graphical user interface (GUI) that allows users to choose the solving algorithm from Depth-First Search (DFS), Breadth-First Search (BFS), and Depth-Limited Search (DLS). For each solving attempt, the execution time of the selected algorithm is displayed, enabling comparison of algorithm efficiency.

## Features

- **Multiple Solving Algorithms**: Choose from DFS, BFS, DLS, and A* Search.
- **Execution Time Display**: Compare the efficiency of different algorithms.
- **User-Friendly GUI**: Input the initial state of the Sudoku grid and view the solution.
- **Expandable**: Potential to handle larger n×n Sudoku grids.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/aplusInDev/sudoku_lab.git
    cd sudoku_lab
    ```

## Usage

1. **Run the application**:

    ```bash
    python main.py
    ```

2. **Input the Sudoku puzzle**:
    - Click on "Load Default" button to load a default puzzle.

3. **Select the solving algorithm**:
    - Choose from DFS, BFS, DLS, or A* Search.

4. **Solve the puzzle**:
    - Click the "Solve" button to start the solving process.
    - The solution will be displayed in the GUI.
    - The execution analysis for the used algorithm will displayed in the terminal.

## How It Works

The project includes the following key components:

- **Node Class**: Encapsulates a state, its parent state, the list of child states, and the action that led to this state.
- **Problem Class**: Formulates the Sudoku problem, defining the initial state, goal state, transition model, goal test function, and cost calculation function.
- **SudokuSolver Class**: Implements the DFS, BFS, DLS, and A* Search algorithms to solve the Sudoku puzzle. It also calculates and displays the execution time for each algorithm.
- **SudokuApp Class**: Provides a user-friendly GUI for inputting the Sudoku puzzle, selecting the solving algorithm, and displaying the solution.

## Example

Here is an example of a Sudoku puzzle and its solution:

### Puzzle

```bash
5 3 0 | 0 7 0 | 0 0 0
6 0 0 | 1 9 5 | 0 0 0
0 9 8 | 0 0 0 | 0 6 0
------+-------+------
8 0 0 | 0 6 0 | 0 0 3
4 0 0 | 8 0 3 | 0 0 1
7 0 0 | 0 2 0 | 0 0 6
------+-------+------
0 6 0 | 0 0 0 | 2 8 0
0 0 0 | 4 1 9 | 0 0 5
0 0 0 | 0 8 0 | 0 7 9
```

### Solution

```bash
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
------+-------+------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
------+-------+------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code follows the project's coding standards and includes appropriate tests.
