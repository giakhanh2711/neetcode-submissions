# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = 0
        mul1, mul2 = 1, 1
        while l1:
            total += mul1 * l1.val
            mul1 *= 10
            l1 = l1.next
        
        while l2:
            total += mul2 * l2.val
            mul2 *= 10
            l2 = l2.next
        
        head = ListNode()
        if total == 0:
            return head
            
        cur = head
        while total:
            cur.next = ListNode(total % 10)
            total //= 10
            cur = cur.next
        
        return head.next