# SUDOKU LAB

## Table of contents

* [Description](#description)
* [How to run](#how-to-run)
* [How to use](#how-to-use)
* [How it works](#how-it-works)
* [Example](#example)

## Description

This is a simple sudoku solver that uses backtracking to solve the puzzle. The program reads the puzzle from a file and then solves it. The program then writes the solution to a file. The program also times how long it takes to solve the puzzle.

## How to run

To run the program, you need to have python installed on your computer. You can download python from [here](https://www.python.org/downloads/). Once you have python installed, you can run the program by running the following command in the terminal:

```bash
python sudoku.py
```

## How to use

The program reads the puzzle from a file called `puzzle.txt`. The puzzle should be in the following format:

```bash
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

Where `0` represents an empty cell. The program will then solve the puzzle and write the solution to a file called `solution.txt`. The solution will be in the following format:

```bash
1 2 3 4 5 6 7 8 9
4 5 6 7 8 9 1 2 3
7 8 9 1 2 3 4 5 6
2 1 4 3 6 5 8 9 7
3 6 5 8 9 7 2 1 4
8 9 7 2 1 4 3 6 5
5 3 1 6 4 2 9 7 8
6 4 2 9 7 8 5 3 1
9 7 8 5 3 1 6 4 2
```

## How it works

The program uses backtracking to solve the puzzle. The program starts at the first empty cell and tries to fill it with a number between 1 and 9. If the number is valid, the program moves on to the next empty cell and tries to fill it. If the number is not valid, the program backtracks and tries a different number. The program continues this process until all the cells are filled.

## Example

Here is an example of a puzzle:

```bash
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

And here is the solution:

```bash
1 2 3 4 5 6 7 8 9
4 5 6 7 8 9 1 2 3
7 8 9 1 2 3 4 5 6
2 1 4 3 6 5 8 9 7
3 6 5 8 9 7 2 1 4
8 9 7 2 1 4 3 6 5
5 3 1 6 4 2 9 7 8
6 4 2 9 7 8 5 3 1
9 7 8 5 3 1 6 4 2
```
