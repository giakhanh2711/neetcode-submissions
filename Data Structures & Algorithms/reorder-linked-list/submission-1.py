# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head

        queue = deque()
        cur = head.next
        while cur:
            queue.append(cur)
            cur = cur.next
        
        cur = head
        flip = 1
        while len(queue) > 0:
            if not flip:
                cur.next = queue.popleft()
                flip = 1
            else:
                cur.next = queue.pop()
                flip = 0
            cur = cur.next
        
        cur.next = None