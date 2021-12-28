# SudokuSolver
This project will solve any sudoku puzzle.
To use the sudoku solver, run "sudoku_solver.py" in the command line using one required argument and one optional argument.

Arguments:
First Argument: Filename - This arugment should be the filename of the file that contains the input sudoku board. The input sudoku board should be in a specific configuration and should also be inside of the directory "in". To see an example of the correct configuration, look at "board2.csv" in the "in" directory.
Second Argument: Output Type - If you wish to output the solution in the command line, you do not have to provide anything for this argument. If you wish to output the solution to a file, then provide "f" or "file" for this argument.

Input file should be put into the "in" directory.
All output files will be written to the "out" directory. They will carry the same name as the provided input file name except with "_solution" included. For example: 
    input file name = board.csv
    ouput file name = board_solution.csv