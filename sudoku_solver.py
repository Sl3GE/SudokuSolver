from typing import List
from Sudoku import Sudoku


def sudokuBacktrackSolver(stateList: List[Sudoku], depth: int):
    state: Sudoku = stateList[0]
    if (state.isBoardComplete()):
        return state
    rules = state.getNextSlotRules()
    for rule in rules:
        newState = state.applyRule(rule)
        if (newState.isBoardValid()):
            result = sudokuBacktrackSolver(
                [newState] + copy.deepcopy(stateList), depth+1)
            if (isinstance(result, Sudoku)):
                return result
    return False


if __name__ == "__main__":
    import sys
    args = sys.argv
    numOfArgs = len(args)
    if (numOfArgs == 1):
        print("Filename not provided")
    else:
        outputType = "c"
        if (numOfArgs > 2 and args[2] in ["f", "file"]):
            outputType = "f"
        fileName = args[1]
        fileInput = Sudoku.readSudokuFromFile("in/"+fileName)
        tempBoard = Sudoku.createBoard(fileInput)
        sudoku = Sudoku(tempBoard)
        result = sudokuBacktrackSolver([sudoku], 0)
        if (outputType == "c"):
            print("Initial Board:\n" + sudoku.getGrid())
            print("\nSolution Board:\n" + result.getGrid())
        else:
            newFileName = fileName[:-4]+"_solution"+fileName[-4:]
            newFile = open("out/"+newFileName, "w")
            newFile.write("Input:\n"+fileInput+"\nSolution:\n"+str(result))
            newFile.close()
