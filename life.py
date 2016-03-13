from structures.array import Array2D

class LifeGrid :
    DEAD_CELL = 0
    LIVE_CELL = 1

    #Creates a life grid and initializes the cells to dead
    def __init__ (self, numRows, numCols):
        self._grid=Array2D(numRows,numCols)
        self.configure(list())

    def numRows (self):
        return self._grid.numRows();

    def numCols(self):
        return self._grid.numCols();

    def configure(self, coordList):
        #Clear the grid
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.clearCell(i,j)

        #Set the indicated cells to be live
        for coord in coordList:
            self.setCell(coord[0],coord[1])

    def isLiveCell(self, row, col):
        return self._grid[row,col] == LifeGrid.LIVE_CELL

    def clearCell(self, row, col):
        self._grid[row,col] == LifeGrid.DEAD_CELL

    def setCell(self, row, col):
        self._grid[row,col] = LifeGrid.LIVE_CELL

    def numLiveNeighbors (self, row,col):
        neighbors=0
        for i in range(row-1,row+2):
            for j in range (col-1,col+2):
                if ( i>0 and i< self.numRows() and j>0 and j< self.numCols() and self.isLiveCell(row,col)):
                    if i==row and j == col:
                        neighbors+=0
                    else:
                        neighbors=neighbors+1
        return neighbors
