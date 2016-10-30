#Modified version of the binary search that returns the index within
#a sorted sequence indicating where the target should be located. 
def findSortedPosition(theList, target):
    low=0
    high=len(theList)-1
    while low <= high:
        mid= (high+low)//2
        if theList[mid] == target:
            return mid
        elif target < theList[mid]:
            high=mid-1
        else:
            low=mid+1 #Index where the target should be
    return low