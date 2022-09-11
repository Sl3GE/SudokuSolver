import copy
from math import floor
 

class Sudoku:
    def __init__(self, board: list[list[str]]):
        self.board = board
        return

    def __str__(self) -> str:
        result = ""
        for row in self.board:
            for i in range(8):
                result += row[i]+","
            result += row[8]+"\n"
        return result

    def __eq__(self, obj) -> bool:
        if (not isinstance(obj, Sudoku)):
            return False
        return self.board == obj.board

    def getGrid(self) -> str:
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
    
    def toCsv(self) -> str:
        result = ""
        for row in self.board:
            first = True
            for slot in row:
                if first:
                    first = False
                else:
                    result += ","
                result += slot
            result += "\n"
        return result

    def getAllRules(self) -> list[list[int]]:
        rules = []
        for i in range(9):
            for j in range(9):
                if (self.board[i][j] == ""):
                    for k in range(1, 10):
                        rules.append([i, j, k])
        return rules

    # O(n^2)
    def getNextSlotRules(self) -> list[list[int]]:
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


    def applyRule(self, rule: list[int]):
        """Apply rule to Sudoku board to make move
        
        Rule should be in the form of [int, int, int]
        where each int is represented by the following
        [row, column, value].
        """
        newSudoku = copy.deepcopy(self)
        newSudoku.board[rule[0]][rule[1]] = str(rule[2])
        return newSudoku
    
    def applyRuleSafely(self, rule: tuple[int,int,int]) -> bool:
        """Apply rule safely to Sudoku board to make move
        
        Rule should be in the form of (int,int,int)
        where each int is represented by the following
        (row, column, value).
        
        It applies the rule safely by also checking if the
        move was valid. If the move breaks any of the
        sudoku rules or a digit already exists in that position,
        then it won't apply the rule and will return False.
        Otherwise, it will apply the rule and return True.
        """
        if (self.board[rule[0]][rule[1]] != ""):
            return False
        self.board[rule[0]][rule[1]] = str(rule[2])
        if (self.isSlotValid((rule[0],rule[1]))):
            return True
        self.board[rule[0]][rule[1]] = ""
        return False

    def isSlotValid(self, slotPos: tuple[int,int]) -> bool:
        slotRow = slotPos[0]
        slotCol = slotPos[1]
        slotValue = self.board[slotRow][slotCol]
        
        for i in range(9):
            # Check Col Slot
            if (slotCol != i and slotValue == self.board[slotRow][i]):
                return False
            # Check Row Slot
            if (slotRow != i and slotValue == self.board[i][slotCol]):
                return False
        # Check Square
        squarePos = (floor(slotRow/3)*3, floor(slotCol/3)*3)
        squareItems = set()
        for k in range(3):
            for l in range(3):
                tempSlot = self.board[squarePos[0]+k][squarePos[1]+l]
                if (tempSlot in squareItems):
                    return False
                if (tempSlot != ""):
                    squareItems.add(tempSlot)
        return True

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

    def isBoardComplete(self) -> bool:
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
    def createBoard(config: str) -> list[list[str]]:
        newBoard: list[list[str]]
        newBoard = []
        rows = config.split("\n")
        for i in range(9):
            newBoard.append(rows[i].split(","))
        return newBoard

    @staticmethod
    def readSudokuFromFile(fileName: str) -> str:
        f = open(fileName, "r")
        lines = ""
        for i in range(9):
            lines += f.readline()
        f.close()
        return lines