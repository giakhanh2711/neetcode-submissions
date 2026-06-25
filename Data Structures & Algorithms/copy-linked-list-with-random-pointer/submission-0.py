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
        dummy = Node(0)
        copy_head = dummy
        cur = head
        while cur:
            copy_head.next = Node(cur.val)
            copy_head = copy_head.next
            cur = cur.next
        
        cur = head
        copy_head = dummy.next

        while cur:
            random_node = head
            random_copy_node = dummy.next
            while random_node:
                if random_node == cur.random:
                    copy_head.random = random_copy_node
                    break
                random_node = random_node.next
                random_copy_node = random_copy_node.next
            
            cur = cur.next
            copy_head = copy_head.next
        
        return dummy.next
