# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(head1, head2, carry):
            if not head1 and not head2 and not carry:
                return None
            v1 = head1.val if head1 else 0
            v2 = head2.val if head2 else 0
            
            val = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) // 10
            
            head = ListNode(val)
            next1 = head1.next if head1 else None
            next2 = head2.next if head2 else None
            head.next = helper(next1, next2, carry)

            return head
        
        return helper(l1, l2, 0)