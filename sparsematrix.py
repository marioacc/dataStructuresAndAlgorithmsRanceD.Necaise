#Implementation of the Sparse Matrix ADT using List
class SparseMatrix:
	def __init__(self,numRows,numCols):
		self._numRows=numRows
		self._numCols=numCols
		self._elementList=list()

		#Return the number of rows in the matrix
		def numRows(self):
			return self._numRows

		#Return the number of columns in the matrix
		def numCols(self):
			return self._numCols

		#Return the value of element  (i,j): x[i,j]
		def __getitem__(self,ndxTuple):

		#Set value of element (i,j) to the value s:x[i,j]=s
		def __setitem__(self,ndxTuple,scalar):
			ndx=self._findPosisiton(ndxTuple[0],ndxTuple[1])
			if ndx is not None: #if element is in the list
				if scalar != 0.0:
					self._elementList[ndx].value=scalar
				else:
					self._elementList.pop(ndx)
			else:	#if the element is zero and non in the list
				if scalar !=0.0:
					element=_MatrixElement(ndxTuple[0],ndxTuple[1],scalar)
					self._elementList.append(element)

		#Scale the matriz by the given scalar
		def scaleBy (self,scalar):
			for element in self._elementList:
				element.value*=scalar
		#Addtional methos should be placed here
		#def __add__(self,rhsMatrix)
		def __add__ (self,rhsMatrix):
			assert rhsMatrix.numRows() == self.numRows and \
				rhsMatrix.numCols() == self.numCols,\
				"Matriz sizes not compatible for the add operation"

			#Create new matrix 
			newMatrix= SparseMatrix(self.numRows(), self.numCols())

			#Duplicate the lhs matrix. The elements are mutable, thus we must 
			#create new objects and not simply copy the reference
			for element in self.elements:
				dupElement= _MatrixElement(element.row,element.col,element.value)
				newMatrix._elementList.append(dupElement)

			for element in rhsMatrix._elementList:
				#Get the value of the corresponding element in the matrix
				value = newMatrix[element.row,element.col]
				value+=element.value
				#Store the new value back to the new matrix
				newMatrix[element.row,element.col]=value

			return newMatrix
		#def __sub__(self,rhsMatrix)
		def __sub__ (self,rhsMatrix):
			assert rhsMatrix.numRows() == self.numRows and \
				rhsMatrix.numCols() == self.numCols,\
				"Matriz sizes not compatible for the add operation"

			#Create new matrix 
			newMatrix= SparseMatrix(self.numRows(), self.numCols())

			#Duplicate the lhs matrix. The elements are mutable, thus we must 
			#create new objects and not simply copy the reference
			for element in self.elements:
				dupElement= _MatrixElement(element.row,element.col,element.value)
				newMatrix._elementList.append(dupElement)

			for element in rhsMatrix._elementList:
				#Get the value of the corresponding element in the matrix
				value = newMatrix[element.row,element.col]
				value-=element.value
				#Store the new value back to the new matrix
				newMatrix[element.row,element.col]=value

			return newMatrix
		#def __mul__(self,rhsMatrix)
		def __mul__ (self,rhsMatrix):
			assert rhsMatrix.numRows() == self.numRows and \
				rhsMatrix.numCols() == self.numCols,\
				"Matriz sizes not compatible for the add operation"

			#Create new matrix 
			newMatrix= SparseMatrix(self.numRows(), self.numCols())

			#Duplicate the lhs matrix. The elements are mutable, thus we must 
			#create new objects and not simply copy the reference
			for element in self.elements:
				dupElement= _MatrixElement(element.row,element.col,element.value)
				newMatrix._elementList.append(dupElement)

			for element in rhsMatrix._elementList:
				#Get the value of the corresponding element in the matrix
				value = newMatrix[element.row,element.col]
				value*=element.value
				#Store the new value back to the new matrix
				newMatrix[element.row,element.col]=value

			return newMatrix

		#Helper methos used to find a specific matrix element (row,col)in the
		#list of non-zero entries. None is returned if the element is not found
		def _findPosition (self,row,col):
			n = len (self._elementList)
			for i in range(n):
				if row== self._elementList[i].row and \
					col ==self._elementList[i].col:
					return i; 
			return None 

		def __add__ (self,rhsMatrix):
			assert rhsMatrix.numRows() == self.numRows and \
				rhsMatrix.numCols() == self.numCols,\
				"Matriz sizes not compatible for the add operation"

			#Create new matrix 
			newMatrix= SparseMatrix(self.numRows(), self.numCols())

			#Duplicate the lhs matrix. The elements are mutable, thus we must 
			#create new objects and not simply copy the reference
			for element in self.elements:
				dupElement= _MatrixElement(element.row,element.col,element.value)
				newMatrix._elementList.append(dupElement)

			for element in rhsMatrix._elementList:
				#Get the value of the corresponding element in the matrix
				value = newMatrix[element.row,element.col]
				value+=element.value
				#Store the new value back to the new matrix
				newMatrix[element.row,element.col]=value

			return newMatrix



		#Storage class for holding the non-zero matrix elements
		class _MatrixElement(self):
			"""docstring for _MatrixElement"""
			def __init__(self, row,col,value):
				self.row=row
				self.col=col
				self.value=value

				



