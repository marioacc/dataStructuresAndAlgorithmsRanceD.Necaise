class Map:
    def __init__(self):
        self._entryList= List()

    def __len__(self):
        return len(self._entryList)

    def __contains__ (self, key):
        ndx = self._findPosition(key)
        return ndx is not None

    def add(self, key, value):
        ndx = self._findPosition(key)
        if ndx is not None:
            self._entryList[ndx].value=value
            return False
        else:
            entry = _MapEntry(key,value)
            self._entryList.append(entry)
            return True

    def valueOf (self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, "Invalid map key"
        return self._entryList[ndx].value

    def remove (self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, "Invalid map key"
        return self._entryList.pop(ndx)

    def __iter__ (self):
        return _MapIterator(self._entryList)

    def _findPosition(self, key):
        for i in range(len(self)):
            if self._entryList[i].key == key:
                return i
        return None

    def _MapEntry(self, key, value):
        self.key =key
        self.value = value

    class _MapIterator:
        def __init__ (self, theList):
            self._listRef = theList
            self._curNdx = 0

        def __iter__ (self):
            return self

        def __next__(self):
            if (self._curNdx < len(self._listRef)):
                entry = self._listRef[self._curNdx]
                self._curNdx+=1
            else:
                raise StopIteration
