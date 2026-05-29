class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        i = 1
        while i <= n and right:
            right = right.next
            i += 1

        while right:
            left = left.next
            right = right.next
        
        #delete
        left.next = left.next.next
        return dummy.next