class Node:
    def __init__(self, data):
        self.next= None
        self.data = data
class LinkedList:
    def __init__(self):
        self.head = None
        
    def display(self): #printong the list
        if self.head is None:
            print("list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->" ,end = "")
                temp = temp.next
                
    def reverse_linked_list(self):
        temp = None
        prev = None
        cur = self.head 
        while  cur:
            temp = cur.next 
            cur.next = prev
            prev = cur
            cur = temp
        self.head = prev 
        self.display()
            
l = LinkedList()
n1 = Node(10)
n2= Node(20)
n3= Node(30)
n4= Node(40)
n5=Node(50)
n6 = Node(60)
n7= Node(50)
l.head = n1
l.head.next=n2
l.head.next.next = n3
l.head.next.next.next = n4
l.head.next.next.next.next = n5
l.head.next.next.next.next.next=n7
l.head.next.next.next.next.next.next = n6
l.reverse_linked_list()
