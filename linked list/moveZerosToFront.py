class Node:
    def __init__(self, data):
        self.next= None
        self.data = data
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->" ,end = "")
                
                temp = temp.next

    def zeros(self):
        prev = self.head
        cur = self.head.next
        while cur!=None:
            if cur.data != 0:
                prev = cur
                cur = cur.next
            else:
                
                prev.next = cur.next
                cur.next = self.head
                self.head = cur
                cur = prev.next
        self.display()
            
l = LinkedList()



n1 = Node(0)
n2= Node(20)
n3= Node(30)
n4= Node(0)
n5=Node(50)
n6 = Node(60)
n7= Node(0)
l.head = n1
l.head.next=n2
l.head.next.next = n3
l.head.next.next.next = n4
l.head.next.next.next.next = n5
l.head.next.next.next.next.next=n7
l.zeros()

'''
output:
0 -->20 -->30 -->0 -->50 -->0 -->original linked list
0 -->0 -->0 -->20 -->30 -->50 -->
'''
