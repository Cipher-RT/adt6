# You can remove 'pass' if you written code in the function
# Each node is a list: [Data, Pointer]. A pointer of -1 means "points to nothing".
from pickle import GLOBAL

# Exercise 1
LinkedList = []
for x in range(8):
    LinkedList.append([-1, x + 1])
LinkedList[7][1] = -1
FirstNode = -1
FirstEmpty = 0


# Write code here to fill LinkedList with 8 nodes (see README)


def IsEmpty():
    # Write your code here
    if FirstNode == -1:
        return True
    return False
    pass


def IsFull():
    # Write your code here
    if FirstEmpty == -1:
        return True
    return False
    pass


# Exercise 2
def Traverse():
    # Write your code here
    global LinkedList, FirstNode
    cur_pointer = FirstNode
    output = []
    while cur_pointer != -1:
        output.append(LinkedList[cur_pointer][0])
        cur_pointer = LinkedList[cur_pointer][1]
    return output
    pass


# Exercise 3
def Search(Item):
    # Write your code here
    global LinkedList, FirstNode, FirstEmpty
    cur_pointer = FirstNode
    while cur_pointer != -1:
        if LinkedList[cur_pointer][0] == Item:
            return cur_pointer
        cur_pointer = LinkedList[cur_pointer][1]
    return -1
    pass


def CountNodes():
    # Write your code here
    pass


# Exercise 4
def InsertFront(Item):
    # Write your code here
    pass


# Exercise 5
def InsertEnd(Item):
    # Write your code here
    pass


# Exercise 6
def Delete(Item):
    # Write your code here
    pass
