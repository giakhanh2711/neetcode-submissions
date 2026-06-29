"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        old_to_copy = {None: None}
        while cur:
            old_to_copy[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            old_to_copy[cur].next = old_to_copy[cur.next]
            old_to_copy[cur].random = old_to_copy[cur.random]
            cur = cur.next
        
        return old_to_copy[head]