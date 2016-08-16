#Sort a sequence in ascending order using the bubble sort algorithm
def bubbleSort(theSeq):
    n=len (theSeq)
    
    #Perform n-1 bubble operations on the sequence
    for i in range(n-1):
        isSorted=True
    #Bubble the largest item to the end
        for j in range(n-1):
            if theSeq[j] > theSeq[j+1]:
                isSorted=False
                tmp=theSeq[j]
                theSeq[j]=theSeq[j+1]
                theSeq[j+1]=tmp
        if isSorted:
            return
                



list=[2, 3, 4, 5, 6, 7, 9, 10]
bubbleSort(list)
print(list)
