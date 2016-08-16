#implementation of the Set ADT container using a Python list
class Set:
    def __init__ (self):
        self._theElements = list()

    #returns number of items in the Set
    def __len__(self):
        return len( self._theElements)

    #Determines if an element is in the Set
    def __contains__ (self, element):
        return element in self._theElements

    #Adds a new unique element to the Set
    def add (self, element):
        if element not in self._theElements
            self._theElements.append(element)

    #Removes an element from the setCell
    def remove(self, element):
        assert element in self, "The element must be in the set"
        self._theElements.remove(element)

    #Determines is two setsare equal
    def __eq__ (self, setB):
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)

    #Determines if this set is subset of setB
    def isSubsetOf(self, setB):
        for element in self
            if element not in self:
                return False
        return True
    def union(self, setB):
        newSet= Set()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
        return newSet

    def intersection(self, setB):
        newSet= Set()
        for element in setB:
            if element in self:
                newSet._theElements.append(element)
        return newSet

    def difference(self, setB):
        newSet= Set()
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
        return newSet

    def __iter__ (self):
        return _SetIterator(self._theElements)

    class _SetIterator:
        def __init__(self, theList):
            self._listRef= theList
            self._curNdx = 0

        def __iter__(self):
            return self

        def  __next__(self):
            if (self._curNdx < len(self._listRef)):
                entry = self._listRef[self._curNdx]
                self._curNdx+=1
                return entry
            else:
                raise StopIteration
