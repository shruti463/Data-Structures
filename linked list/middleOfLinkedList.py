class Node:
    def __init__(self, data):
        self.next= None
        self.data = data
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def display(self): #printing linked list
        if self.head is None:
            print("list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->" ,end = "")
                temp = temp.next
                
    def middle_print(self): #printing middle element
        slow = self.head
        fast= self.head
        while fast!=None and fast.next!=None:
            slow =slow.next
            fast= fast.next.next
        print("\n")
        print("middle element:", slow.data)
                
    def mid_insertion(self, n6): #insertion at middle
        slow = self.head
        fast= self.head.next
        while fast!=None and fast.next!=None:
            slow =slow.next
            fast= fast.next.next
        ele = slow.next
        slow.next = n6
        slow.next.next = ele
        print("\n")
        print("insert at the mid ele")
        self.display()      
        
        
    def mid_deletion(self):  #deleting middle element
        slow = self.head
        fast= self.head
        while fast!=None and fast.next!=None:
            temp = slow
            slow =slow.next
            fast= fast.next.next
        temp.next = slow.next
        print("\n")
        print("ll after deletion")
        self.display()
        
        
    def deletion_after_middle(self):
        slow = self.head
        fast= self.head
        while fast!=None and fast.next!=None:
            temp = slow
            slow =slow.next
            fast= fast.next.next 
        slow.next = slow.next.next
        print("\n")
        print("deletion after middle element")
        self.display()
        
        
    def deletion_before_middle(self):
        slow = self.head
        fast= self.head.next.next
        while fast!=None and fast.next!=None:
            temp = slow
            slow =slow.next
            fast= fast.next.next 
        temp.next = slow.next
        print("deletion before mid element ")
        self.display()
    
    
l = LinkedList()
n1 = Node(10)
n2= Node(20)
n3= Node(30)
n4= Node(40)
n5=Node(50)
n6 = Node(60)
n7= Node(70)
l.head = n1
l.head.next=n2
l.head.next.next = n3
l.head.next.next.next = n4
l.head.next.next.next.next = n5
l.head.next.next.next.next.next=n7
print("original ll")
l.display()
l.middle_print()
l.mid_insertion(n6)
l.mid_deletion()
l.deletion_after_middle()
l.deletion_before_middle()
