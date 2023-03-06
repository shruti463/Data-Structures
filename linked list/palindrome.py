def reverseList(self, head): #reverses second half of the list
        if head == None:
            return head
        if head.next == None:
            return head
        prev = None
        temp = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev
        
def isPalindrome(self, head):
        #middle of list
        slow = head
        fast = head
 
        # Iterate till fast's next is null (fast reaches end)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        first = head
        sloww = self.reverseList(slow)
        #check first half of list with second half
        while first and sloww:
            if first.data !=sloww.data:
                return False
            first = first.next
            sloww = sloww.next
        return True
