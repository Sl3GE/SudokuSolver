from Sudoku import Sudoku

class SudokuFactory:
    def __init__(self, difficulty: int) -> None:
        self.difficulty = difficulty
        return
    
    def createSudoku(self) -> Sudoku:
        boardMatrix = []
        # TODO: create board based on difficulty
        return Sudoku(boardMatrix)