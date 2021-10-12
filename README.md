# DFS_Sudoku_Solver
A depth-first backtracking sudoku solver, written in python

readme.txt
Backtracking Depth-First Search Sudoku Solving Software
v1.0.0
Author: Zac Greene

2021-08

This program can be used to solve sudoku puzzles by using a depth-first
search with backtracking.

The Sudoku puzzle is encoded as an unbroken string of 81 digits. 
This variable is 'importString' and can be found line 34 in solver.py.

The digits represent the cell values in order from top-left to bottom-right.
Empty cells are assigned a 0.

The program can be run from the command line by navigating to the directory
the solver.py file is in, and executing:

python3 solver.py

Command line options are:

-h --help     : shows command line options
-p --print    : enables printing mode, which prints the board after each move.
                The placed value is coloured according to context (value added/removed)
-s --steps    : enables step-by-step solving. The program will prompt from
                user input (enter key) before each move. 
                It is best used with printing on.

The following will solve the puzzle, printing intermediate steps:
python3 solver.py -p

Whereas the following will solve the puzzle, printing intermediate steps,
and prompting the user for input at each stage:
python3 solver.py -p -s

If no command line arguments are given:
python3 solver.py
the program will prompt the user for confimation of options.
Printing and step-by-step options can be enabled by following
the prompts. If invalid values are given, both options are off by default.
