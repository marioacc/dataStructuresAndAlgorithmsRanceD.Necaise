# Implementation of the Set ADT using a sorted list.
class Set:
    # Creates an empty set instance

    def __init__(self):
        self._theElements = list()

    # Returns the number of items in the set
    def __len__(self):
        return len(self._theElements)

    # Determines if an element is in the set.
    def __contains__(self, element):
        ndx = self._findPosition(element)
        return ndx < len(self) and self._theElements[ndx]

    def add(self, element):
        if element not in self:
            ndx = self._findPosition(element)
            self._theElements.insert(ndx, element)

    def remove(self, element):
        assert element in self, "The element must be in the set"
        ndx = self._findPosition(element)
        self._theElements.pop(ndx)

    # Determines if this set is subset of setB
    def isSubsetOf(self, setB):
        if len(self) > len(setB):
            return False
        for i in range(len(self)):
            if self._theElements[i] != setB._theElements[i]:
                return False
        return True

    def union(self, setB):
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
        return newSet

    def intersection(self, setB):
        newSet = Set()
        for element in setB:
            if element in self:
                newSet._theElements.append(element)
        return newSet

    def difference(self, setB):
        newSet = Set()
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
        return newSet

    def __iter__(self):
        return _SetIterator(self._theElements)

    def _eq(self, setB):
        if len(self) != setB:
            return False
        else:
            for i in range(len(self)):
                if self._theElements[i] != setB._theElements[i]:
                    return False
            return True

    # Merges two sorted lists to create and return a new sorted list.

    def union(self, setB):
        # Create a new list and initialize the list markers.
        newSet = Set()
        a = 0
        b = 0

        # Merge the two lists togethe until one is empty
        while a < len(self) and b < len(setB):
            valueA = self._theElements[a]
            valueB = setB._theElements[b]
            if valueA < valueB:
                newSet._theElements.append(valueA)
                a += 1
            elif valueA > valueB:
                newSet._theElements.append(valueB)
                b += 1

        # If listA contains more items, append them to newList
        while a < len(self):
            newSet._theElements.append(valueA)
            a += 1

        # If listA contains more items, append them to newList
        while b < len(setB):
            newSet._theElements.append(valueB)
            b += 1

        return newSet

    def _findPosition(self, element):
        low = 0
        high = len(self) - 1
        while low <= high:
            mid = (high + low) / 2
            if self._theElements[mid] == element:
                return mid
            elif element < self._theElements[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low

    class _SetIterator:

        def __init__(self, theList):
            self._listRef = theList
            self._curNdx = 0

        def __iter__(self):
            return self

        def __next__(self):
            if (self._curNdx < len(self._listRef)):
                entry = self._listRef[self._curNdx]
                self._curNdx += 1
                return entry
            else:
                raise StopIteration
