class Solution:
  #counts the length of both ll
    def count(self,temp):
        c = 0
        while temp:
            c+=1
            temp = temp.next
        return c
        

    def getIntersectionNode(self, h1: ListNode, h2: ListNode) -> Optional[ListNode]:
        temp1 = h1
        temp2 = h2
        c2 =self.count(temp2) 
        c1 =self.count(temp1)
        #find absolute diff b/w the length of ll
        diff = abs(c1-c2)
        if ll1 or ll2 is bigger that other ,so iterate that list so both point at same length index 
        if c1>c2:
            for i in range(diff):
                h1 = h1.next
        else:
            for i in range(diff):
                h2 = h2.next
        while h1 != None and h2 != None:
            if h1 == h2:
                return h1
            h1 = h1.next
            h2 = h2.next
        return None
