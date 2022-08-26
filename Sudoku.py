import copy


class Sudoku:
    def __init__(self, board: List[List[str]]):
        self.board = board

    def __str__(self):
        result = ""
        for row in self.board:
            for i in range(8):
                result += row[i]+","
            result += row[8]+"\n"
        return result

    def getGrid(self):
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

    # O(n^2)
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