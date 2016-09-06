#Sorts a sequence in ascending order using the selection sort 
def selectionSort(theSeq):
    n=len(theSeq)
    for i in range(n-1):
        #Assume the ith element is the smallest
        smallNdx=i
        #Determine if any other element contains a smaller value    
        for j in range (i+1,n):
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx=j
        if smallNdx != i:
            tmp= theSeq[i]
            theSeq[i]=theSeq[smallNdx]
            theSeq[smallNdx]=tmp
    return theSeq

print(selectionSort([4,5,3,2,3,6,8]))