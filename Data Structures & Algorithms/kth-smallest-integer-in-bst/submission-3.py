# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def dfs(node, k):
            if not node:
                return -1
            
            res = dfs(node.left, k)
            if res != -1:
                return res
            
            if k[0] == 1:
                return node.val
            
            k[0] -= 1
            return dfs(node.right, k)
        
        return dfs(root, [k])
