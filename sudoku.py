import random

class board:
    
        def __init__(self):
                self.playingBoard = [
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]

                self.size = len(self.playingBoard)

                self.populateBoard()

        def populateBoard(self):
                empty_cell = self.emptyCellLocator()

                if not empty_cell:
                        return True
                
                i, j = empty_cell
                
                for k in random.sample(range(1, 10), 9):
                        if self.checkCell(i, j, k) == False and self.checkColumn(i, j, k) == False and self.checkRow(i, j, k) == False:
                                self.playingBoard[i][j] = k
                                if self.populateBoard():
                                        return True
                                self.playingBoard[i][j] = 0

                return False


        def emptyCellLocator(self):
                for i in range(self.size):
                        for j in range(self.size):
                                if self.playingBoard[i][j] == 0:
                                        return (i, j)
                return None

        def checkCell(self, row, column, value):
                present = False
                rowMin = self.lowerLimit(row)
                rowMax = row + 1
                columnMin = self.lowerLimit(column)
                columnMax = self.upperLimit(column)

                exit_loops = False
                for i in range(rowMin, rowMax):
                        for j in range(columnMin, columnMax):
                                if i == row and j == column:
                                        exit_loops = True
                                        break
                                if self.playingBoard[i][j] == value:
                                        exit_loops = True
                                        present = True
                                        break
                        if exit_loops:
                                break
                return present

        def checkColumn(self, row, column, value):
                present = False
                i = 0
                while i < row:
                        if self.playingBoard[i][column] == value:
                                present = True
                                break
                        i += 1
                return present
        
        def checkRow(self, row, column, value):
                present = False
                i = 0
                while i < column:
                        if self.playingBoard[row][i] == value:
                                present = True
                                break
                        i += 1
                return present
        

        def printBoard(self):
                for row in self.playingBoard:
                        for element in row:
                                print(element, end = " ")
                        print()

        def lowerLimit(self, val):            
                limit = None
                if val < 3:
                        limit = 0
                elif val < 6:
                        limit = 3
                else:
                        limit = 6
                return limit
        
        def upperLimit(self, val):
                limit = None
                if val < 3:
                        limit = 3
                elif val < 6:
                        limit = 6
                else:
                        limit = 9
                return limit