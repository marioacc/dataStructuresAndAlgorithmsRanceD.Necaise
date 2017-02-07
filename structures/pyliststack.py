#Implementatin of the Stack ADT using pthon list.
class Stack:
    #creates an empty stack
    def __init__(self):
        self._theItems=list()

    #Returns true if the stack is empty, or False otherwise
    def isEmpty(self):
        return len(self)===0

    #Returns the number of items in the Stack
    def __len__(self):
        return len(self._theItems)

    #Returns the top item of the stack without removing it.
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._theItems[-1]

    #Removes and returns the top item on the Stack
    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        return self._theItems.pop()

    #Push an item onto the top of the Stack
    def push(self,item):
        self._theItems.append(item)
               
        