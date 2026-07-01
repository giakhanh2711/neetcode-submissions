# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mul1, mul2 = 1, 1
        total = 0
        head = ListNode()
        while l1 or l2:
            total += mul1 * l1.val if l1 else 0
            mul1 *= 10
            total += mul2 * l2.val if l2 else 0
            mul2 *= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        cur = head
        while total:
            cur.next = ListNode(total % 10)
            total //= 10
            cur = cur.next
        
        return head if not head.next else head.next
