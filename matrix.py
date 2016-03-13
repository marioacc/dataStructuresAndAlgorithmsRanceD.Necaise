import array
from array import Array2D

class Matrix :
    #Creates the matrix, of size numRows X numColumns
    def __init__(self,numRows,numCols):
        self._theGrid = Array2D(numRows,numCols);
        self._theGrid.clear(0)

    def numRows (self):
        return self._theGrid.numRows();

    def numCols (self):
        return self._theGrid.numCols();

    def __getitem__(self, ndxTuple):
        return self._theGrid[ndxTuple[0],ndxTuple[1]]

    def __setitem__(self, ndxTuple, scalar):
        self._theGrid[ndxTuple[0],ndxTuple[1]] = scalar

    def scaleBy(self, scalar):
        for i in range(self.numRows()):
            for j in range( self.numCols()):
                self[i,j] *= scalar

    def transpose (self):
        newMatrix = Matrix(self.numCols(),self.numRows())
        for r in range(self.numRows()):
            for c in range( self.numCols()):
                newMatrix[c,r]=self[r,c]
        return newMatrix

    def __add__(self, rhsMatrix):
        assert rhsMatrix.numRows()==rhsMatrix.numRows()\
            and rhsMatrix.numCols()==rhsMatrix.numCols()\
            , "Matriz size not compatible for operation"
        #create a new matrix
        newMatrix = Matrix(self.numRows(),self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r,c]=self[r,c]+rhsMatrix[r,c]
        return newMatrix

    def __sub__(self, rhsMatrix):
        assert rhsMatrix.numRows()==rhsMatrix.numRows()\
            and rhsMatrix.numCols()==rhsMatrix.numCols()\
            , "Matriz size not compatible for operation"
        #create a new matrix
        newMatrix = Matrix(self.numRows(),self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r,c]=self[r,c]-rhsMatrix[r,c]
        return newMatrix

    def __mul__(self, rhsMatrix):
        assert rhsMatrix.numRows()==rhsMatrix.numRows()\
            and rhsMatrix.numCols()==rhsMatrix.numCols()\
            , "Matriz size not compatible for operation"
        #create a new matrix
        newMatrix = Matrix(self.numRows(),self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r,c]=self[r,c]*rhsMatrix[r,c]
        return newMatrix
