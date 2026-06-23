# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        i = 0
        while i < length - n:
            cur = cur.next
            i += 1
        
        cur.next = cur.next.next

        return dummy.next