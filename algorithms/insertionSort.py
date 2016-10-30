#Sorts a sequence in ascending order using insertion sort
def insertionSort(theSeq):
    n=len(theSeq)
    #Starts with the first item as the only sorted entry
    for i in range(i,n):
        #Save the value to be positionated
        value=i
        #Find the positin where value fits in the ordered part of the List
        pos=i
        while pos>0 and value < theSeq[pos -1]:
            theSeq[pos] = theSeq[pos -1]
            pos-=1
            

