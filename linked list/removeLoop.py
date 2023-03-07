
class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        slow = head
        fast = head
        prev = None
        
        while fast!=None and fast.next!=None :
            prev = slow
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
            
        if fast !=slow: #when both are none
            return
    
        slow = head
        if fast==slow: #when both are head
            prev.next=None #last element
        else:
            while fast.next!=slow.next: #no need of prev
                fast = fast.next
                slow = slow.next
            fast.next = None
       
        

