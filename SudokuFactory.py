from random import Random
from Sudoku import Sudoku
from sudoku_solver import sudokuBacktrackSolver

class SudokuFactory:
    
    __random = Random()
    
    def __init__(self, difficulty: int) -> None:
        if difficulty < 1:
            self.difficulty = 1
        elif difficulty > 10:
            self.difficulty = 10
        else:
            self.difficulty = difficulty
        return
    
    def __genRandomSudokuNum__(self) -> int:
        return self.__random.randint(0,8)
    
    def createSudoku(self) -> Sudoku:
        boardMatrix = [["" for i in range(9)] for j in range(9)]
        sudoku = Sudoku(boardMatrix)
        result = sudokuBacktrackSolver([sudoku],0)
        numOfRemovals = 20 + (self.difficulty * 8)
        for i in range(numOfRemovals):
            col = self.__genRandomSudokuNum__()
            row = self.__genRandomSudokuNum__()
            result = result.applyRule([row,col,""])
        return result

if __name__ == "__main__":
    import sys
    args = sys.argv
    numOfArgs = len(args)
    if (numOfArgs == 1):
        print("Difficulty was not provided")
        exit(1)
    outputType = "c"
    if (numOfArgs > 2 and args[2] in ["f", "file"]):
        outputType = "f"
    difficulty: int
    try:
        difficulty = int(args[1])
    except:
        print("Difficulty argument requires an integer")
        exit(1)
    factory = SudokuFactory(difficulty)
    sudoku = factory.createSudoku()
    if (outputType == "c"):
        print(sudoku.getGrid())
    else:
        # TODO: add code for generating filenames based on datetime and possibly random characters
        # newFileName = fileName[:-4]+"_solution"+fileName[-4:]
        # newFile = open("out/"+newFileName, "w")
        # newFile.write("Input:\n"+fileInput+"\nSolution:\n"+str(result))
        # newFile.close()
        exit(0)
    