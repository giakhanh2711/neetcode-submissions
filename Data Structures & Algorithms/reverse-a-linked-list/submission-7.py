# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        sub = self.reverseList(head.next)
        if sub:
            head.next.next = head
            head.next = None
            return sub
        
        return head