class Node:
    def __init__(self, data):
        self.next= None
        self.data = data
class LinkedList:
    def __init__(self):
        self.head = None
        
    def display(self): #printing the linked list
        if self.head is None:
            print("list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->" ,end = "")
                temp = temp.next
                
    def insert(self, x):
        if self.head ==None:
            self.head = x
            
        cur = self.head
        if cur.data >= x.data: #insertion at begining corner case
            x.next = cur
            self.head = x
            print("\n")
            self.display()
        else:
            while cur.next!=None and cur.next.data < x.data :
                cur=cur.next
            temp = cur.next
            cur.next=x
            cur.next.next = temp
            print("\n")
            self.display()
            
         
                 
                 
l = LinkedList()
n1 = Node(10)
n2= Node(20)
n3= Node(30)
n4= Node(40)
n6=Node(50)
l.head = n1
l.head.next=n2
l.head.next.next = n3
l.head.next.next.next = n4
l.head.next.next.next.next = n6
n5 = Node(6)
l.display()
l.insert(n5)
