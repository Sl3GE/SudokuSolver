import copy
from typing import List


class Sudoku:
    def __init__(self, board: List[List[str]]):
        self.board = board

    def __str__(self):
        boxLayerStr = "+---+---+---+"
        result = boxLayerStr
        for i in range(0, 9, 3):
            result += "\n"
            for j in range(3):
                result += "|"
                for k in range(0, 9, 3):
                    for l in range(3):
                        value = self.board[i+j][k+l]
                        if (value == ""):
                            result += " "
                        else:
                            result += str(self.board[i+j][k+l])
                    result += "|"
                result += "\n"
            result += boxLayerStr
        return result

    def __eq__(self, obj):
        if (not isinstance(obj, Sudoku)):
            return False
        return self.board == obj.board

    def getAllRules(self):
        rules = []
        for i in range(9):
            for j in range(9):
                if (self.board[i][j] == ""):
                    for k in range(1, 10):
                        rules.append([i, j, k])
        return rules

    def getNextSlotRules(self):
        rules = []
        amtOfRules = 10
        for i in range(9):
            for j in range(9):
                if (self.board[i][j] == ""):
                    availableValues = {"1", "2", "3",
                                       "4", "5", "6", "7", "8", "9"}
                    for slot in self.board[i]:
                        if (slot in availableValues):
                            availableValues.remove(slot)
                    for row in range(9):
                        slot = self.board[row][j]
                        if (slot in availableValues):
                            availableValues.remove(slot)
                    availableSize = len(availableValues)
                    if (availableSize < amtOfRules):
                        rules = []
                        for k in availableValues:
                            rules.append([i, j, int(k)])
                        amtOfRules = availableSize
        return rules

    def applyRule(self, rule: List[int]):
        newSudoku = copy.deepcopy(self)
        newSudoku.board[rule[0]][rule[1]] = str(rule[2])
        return newSudoku

    def isBoardValid(self):
        # First, Check Rows
        for row in self.board:
            rowItems = set()
            for slot in row:
                if (slot in rowItems):
                    return False
                if (slot != ""):
                    rowItems.add(slot)
        # Second, Check Cols
        for col in range(9):
            colItems = set()
            for row in range(9):
                slot = self.board[row][col]
                if (slot in colItems):
                    return False
                if (slot != ""):
                    colItems.add(slot)
        # Third, Check Squares
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                squareItems = set()
                for k in range(3):
                    for l in range(3):
                        slot = self.board[i+k][j+l]
                        if (slot in squareItems):
                            return False
                        if (slot != ""):
                            squareItems.add(slot)
        return True

    def isBoardComplete(self):
        # First, Check Rows
        for row in self.board:
            rowItems = set()
            for slot in row:
                if (slot in rowItems):
                    return False
                if (slot == ""):
                    return False
                rowItems.add(slot)
        # Second, Check Cols
        for col in range(9):
            colItems = set()
            for row in range(9):
                slot = self.board[row][col]
                if (slot in colItems):
                    return False
                colItems.add(slot)
        # Third, Check Squares
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                squareItems = set()
                for k in range(3):
                    for l in range(3):
                        slot = self.board[i+k][j+l]
                        if (slot in squareItems):
                            return False
                        squareItems.add(slot)
        return True

    @staticmethod
    def createBoard(config: str):
        newBoard: list[list[str]]
        newBoard = []
        rows = config.split("\n")
        for i in range(9):
            newBoard.append(rows[i].split(","))
        return newBoard

    @staticmethod
    def readSudokuFromFile(fileName: str):
        f = open(fileName, "r")
        lines = ""
        for i in range(9):
            lines += f.readline()
        f.close()
        return(lines)


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
    if (len(args) > 1):
        fileName = args[1]
        tempBoard = Sudoku.createBoard(Sudoku.readSudokuFromFile(fileName))
    else:
        # solution:
        # tempBoard = Sudoku.createBoard(
        #    "5,3,4,6,7,8,9,1,2\n6,7,2,1,9,5,3,4,8\n1,9,8,3,4,2,5,6,7\n8,5,9,7,6,1,4,2,3\n4,2,6,8,5,3,7,9,1\n7,1,3,9,2,4,8,5,6\n9,6,1,5,3,7,2,8,4\n2,8,7,4,1,9,6,3,5,\n3,4,5,2,8,6,1,7,9")
        tempBoard = Sudoku.createBoard(
            "5,3,,,7,,,,\n6,,,1,9,5,,,\n,9,8,,,,,6,\n8,,,,6,,,,3\n4,,,8,,3,,,1\n7,,,,2,,,,6\n,6,,,,,2,8,\n,,,4,1,9,,,5\n,,,,8,,,7,9")
    sudoku = Sudoku(tempBoard)
    print("Initial Board:\n" + str(sudoku))
    result = sudokuBacktrackSolver([sudoku], 0)
    print("\nSolution Board:\n" + str(result))
