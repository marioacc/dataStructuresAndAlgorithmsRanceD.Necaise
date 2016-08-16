from structures.array import MultiArray

multiArray= MultiArray(3,3,3)
assert multiArray.numDims() ==3 , "The number of dimensions is not correct"
assert multiArray.length(1) == 3,"The length of the dimension is not correct"
multiArray.clear(5)
multiArray[0,0,2]=7
assert multiArray[0,0,2]==7,"The class is not setting the values in the correct space"
