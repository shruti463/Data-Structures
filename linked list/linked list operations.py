class Node:
    def __init__(self, data) :
        self.data = data 
        self.next= None     #address of next node  
class LinkedList:
    def __init__(self) :
        self.head = None
        
    def display(self): #printing the linked list  and its length
        self.count = 0
        if self.head is None:
            print("list is empty")
        else:
            temp = self.head
            while temp:
                self.count +=1
                print(temp.data ,"-->", end = "")
                temp = temp.next
            print("\n")
            print(self.count) #printing length of the linked list
                
                
                
    def insert_at_begining(self, node, n1):
        if self.head is None:
            self.head = node
            self.display()
        else:
            self.head = node
            self.head.next=n1
            
            print("\n new ll after insert at begining")
            self.display()
                
            print("\n")
            
            
    def insert_at_end(self, node):
        if self.head is None:
            self.head = node
            self.display()
        else:
            temp = self.head
            while temp.next !=None:
                temp = temp.next
            temp.next = node
            print("new ll after insertion at end")
            self.display()
                
                      
    def deletion_at_begining(self):
        if self.head is None:
                print("list is empty")
        else:
            print("\n ll after delete at begining")
            self.head = self.head.next
            self.display()
            
        
    def deletion_at_end(self):
        if self.head is None:
            print("list is empty")
            
        elif self.head.next == None:
            self.head = None   #one node only
            self.display()
            
        else:
            print("\n  ll after delete at end")
            temp = self.head
            while temp.next.next :
                temp = temp.next
            temp.next = None
            self.display()
            
            
    def search(self, x): #searching an element in the linked list
        temp = self.head
        pos = 1
        while temp:
            if temp.data == x:
                return pos
            elif temp.next is None:
                return -1
            pos+=1
            temp = temp.next    
                        
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
l = LinkedList()
l.head = n1
l.head.next= Node(20)


l.head.next.next = Node(30)
l.head.next.next.next = Node(40)
l.display()
l.insert_at_begining(Node(50), n1)
l.insert_at_end(Node(60))
l.deletion_at_begining()
l.deletion_at_end()

print("pos: ",l.search(40))


