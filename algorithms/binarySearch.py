def binarySearch (theValues,target):
    #Start with the entire sequence of elements
    low = 0
    high=len(theValues)-1
    #Repeteadly divide the sequence in half until the target is found
    while low <= high:
        #find the midpoint sequence
        mid= (high+low)//2

        #Does the midpoint contain the target
        if theValues[mid] == target:
            return True
        #or does the target precede the midpoint
        elif target < theValues[mid]:
            high = mid-1
        else:
        #Does it follow the midpoint
            low=mid+1
    return False