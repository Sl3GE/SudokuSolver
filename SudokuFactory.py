from random import Random
from Sudoku import Sudoku
from sudoku_solver import sudokuBacktrackSolver

class SudokuFactory:
    def __init__(self, difficulty: int) -> None:
        if difficulty < 1:
            self.difficulty = 1
        elif difficulty > 10:
            self.difficulty = 10
        else:
            self.difficulty = difficulty
        return
    
    def createSudoku(self) -> Sudoku:
        boardMatrix = [["" for i in range(9)] for j in range(9)]
        sudoku = Sudoku(boardMatrix)
        result = sudokuBacktrackSolver([sudoku],0)
        numOfRemovals = 20 + (self.difficulty * 8)
        random = Random()
        for i in range(numOfRemovals):
            col = random.randint(0,8)
            row = random.randint(0,8)
            result = result.applyRule([row,col,""])
        return result

if __name__ == "__main__":
    factory = SudokuFactory(5)
    sudoku = factory.createSudoku()
    print(sudoku.getGrid())