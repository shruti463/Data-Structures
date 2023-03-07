 def countNodesinLoop(head):
        if head == None or head.next==None:
                return None
        slow = head
        fast = head
        count = 0
        #checks for loop
        while fast!=None and fast.next!=None :
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if fast!=slow : #if no loop
            return 0
        else:
            slow = head
            while fast!=slow:
                slow = slow.next
                fast = fast.next
            #slow is the begin node of loop
            temp = slow.next
            while temp!=slow:
                count+=1
                temp = temp.next
            return count+1
        return 0
