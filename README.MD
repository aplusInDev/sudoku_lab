# Sudoku Solver Based on AI Search Algorithms

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Technical Requirements](#technical-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithm Details](#algorithm-details)
- [Performance Analysis](#performance analysis)
- [Project Structure](#project-structure)
- [Example](#example)
- [Contributing](#contributing)

## Description

This project implements an intelligent Sudoku solver using various artificial intelligence search algorithms. Built with Python, it features a graphical user interface (GUI) that allows users to experiment with different solving strategies including Depth-First Search (DFS), Breadth-First Search (BFS), and Depth-Limited Search (DLS). The solver not only finds solutions but also provides detailed performance metrics, making it an excellent tool for both solving Sudoku puzzles and comparing algorithm efficiency.

## Features

- **Multiple Solving Algorithms**:
  - Depth-First Search (DFS) for memory-efficient solving
  - Breadth-First Search (BFS) for optimal solutions
  - Depth-Limited Search (DLS) for controlled exploration

- **Advanced Performance Analysis**:
  - Real-time execution time measurement
  - Memory usage tracking
  - Node expansion statistics
  - Solution path analysis

- **User-Friendly Interface**:
  - Intuitive puzzle input system
  - Real-time validation of entries
  - Visual solution playback
  - Algorithm comparison dashboard

- **Extensible Architecture**:
  - Support for custom puzzle sizes (n×n)
  - Pluggable algorithm interface
  - Modular design for easy extensions

## Technical Requirements

- Python 3.8 or higher
- Required Python packages:

  ```bash
  tkinter>=8.6
  numpy>=1.19.0
  pytest>=6.0.0 (for testing)
  ```

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/aplusInDev/sudoku_lab.git
    cd sudoku_lab
    ```

## Usage

1. **Launch the application**:

    ```bash
    python main.py
    ```

2. **Input Puzzle**:
    - Enter numbers manually in the grid
    - Use "Load Default" for sample puzzles
    - Import custom puzzles from files

3. **Configure Solver**:
    - Select algorithm from dropdown menu
    - Adjust algorithm parameters (if applicable)
    - Set execution time limits (optional)

4. **Execute and Analyze**:
    - Click "Solve" to start processing
    - View solution progression
    - Examine performance metrics
    - Export results (optional)

## Algorithm Details

### Depth-First Search (DFS)

- **Strategy**: Explores as far as possible along each branch before backtracking
- **Memory Usage**: O(bm) where b is branching factor and m is maximum depth
- **Completeness**: Complete for finite state spaces
- **Time Complexity**: O(b^m) in worst case

### Breadth-First Search (BFS)

- **Strategy**: Explores all nodes at present depth before moving to next level
- **Memory Usage**: O(b^d) where d is solution depth
- **Completeness**: Complete and optimal for unweighted paths
- **Time Complexity**: O(b^d)

### Depth-Limited Search (DLS)

- **Strategy**: DFS with depth cutoff
- **Memory Usage**: O(bl) where l is depth limit
- **Completeness**: Complete up to depth limit
- **Time Complexity**: O(b^l)

## Project Structure

```txt
sudoku_lab/
├── src/
│   ├── algorithms/
│   │   ├── dfs.py
│   │   ├── bfs.py
│   │   └── dls.py
│   ├── gui/
│   │   ├── main_window.py
│   │   └── grid_display.py
│   ├── models/
│   │   ├── sudoku_board.py
│   │   └── node.py
│   └── utils/
│       ├── validator.py
│       └── performance.py
├── tests/
│   ├── test_algorithms.py
│   └── test_validator.py
├── examples/
│   └── puzzles/
├── main.py
└── requirements.txt
```

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

1. Fork the repository
2. Create a feature branch:

    ```bash
    git checkout -b feature/new-feature
    ```

3. Commit changes:

    ```bash
    git commit -m 'Add new feature'
    ```

4. Push to branch:

    ```bash
    git push origin feature/new-feature
    ```

5. Submit a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guide
- Add unit tests for new features
- Update documentation
- Maintain test coverage above 80%
