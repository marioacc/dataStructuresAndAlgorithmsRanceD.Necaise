#Array ADT
import ctypes

class Array:
    def __init__(self, size):
        assert size > 0 , "Array size must be > 0"
        self._size=size
        # Creates the array structure
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(None);

    # Return the length of the array
    def __len__(self):
        return self._size

    # Gets the content of the index element
    def __getitem__(self,index):
        assert index>=0 and index <len(self), "Array subscrit out of range"
        return self._elements[index];

    #Sets a content in the index element
    def __setitem__(self, index, value):
        assert index>=0 and index <len(self), "Array subscrit out of range"
        self._elements[index]=value

    #Clear the array by setting each element to the given value
    def clear(self,value):
        for i in range(len(self)):
            self._elements[i]=value

    #Returns an array iterator for traversing the elements
    def  __iter__ (self):
        return _ArrayIterator(self._elements)
    #Iterator for the arrayADT
    class _ArrayIterator:
        def __init__(self, theArray):
            self._arrayRef= theArray
            self._curNdx = 0

        def __iter__(self):
            return self

        def  __next__(self):
            if (self._curNdx < len(self._arrayRef)):
                entry = self._arrayRef[self._curNdx]
                selc._curNdx+=1
                return entry
            else:
                raise StopIteration

class Array2D:
    #Creates de 2D arrayADT
    def __init__ (self,numRows,numCols):
        self._theRows=Array(numRows)

        #Creates one 1D array for each row of the 2D array
        for i in range(numRows):
            self._theRows[i]= Array(numCols)

    #Returns the num of rows
    def numRows(self):
        return len( self._theRows)

    #Returns the num of columns
    def numCols(self):
        return len( self._theRows[0])

    #Clears the array by setting every element to the given value
    def clear(self, value):
        for row in range(self.numRows()):
            self._theRows[row].clear(value)

    #Gets the content of the element at the position [i,j]
    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "Invalid number of array subscrits"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0  and col < self.numCols(), \
            "Arrayy subscrit out of range"
        the1dArray = self._theRows[row]
        return the1dArray[col]

    #Sets the content of the element at the position [i,j]  to value
    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "Invalid number of array subscrits"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0  and col < self.numCols(), \
            "Arrayy subscrit out of range"
        the1dArray = self._theRows[row]
        the1dArray[col]= value
