class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
      '''
      note: at some point if there is a loop then the fast and slow pointer will meet otherwise there will be no loop
      '''
