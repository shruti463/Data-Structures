import math

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class stack:
    def __init__(self):
        self.head= None
        self.size = 0
        
    def push(self, x):
        
        newnode = Node(x)
        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
        self.size += 1
        
    def pop(self):
        if self.head==None:
            print('-1')
        temp = self.head.data
        self.head = self.head.next
        self.size -=1
        print(temp)
        
    def peek(self):
        if self.head==None:
            print(math.inf)
        else:
            print("peek:",self.head.data)
        
    def isEmpty(self):
        if self.head == None:
            print("list is empty")
        else:
            print("false")
            
    def length(self):
        print("length:",self.size)
        
    def printStack(self):
        temp = self.head
        while temp:
            print(temp.data, "-->", end = "")
            temp = temp.next
        print("\n")


s = stack()
s.peek()
s.push(5)
s.push(4)
s.push(3)
s.push(2)
s.push(1)
s.printStack()

s.pop()
s.printStack()
s.pop()
s.length()
s.peek()
