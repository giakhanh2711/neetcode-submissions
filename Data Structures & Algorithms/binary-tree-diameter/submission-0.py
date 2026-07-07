# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root, max_height):
            if not root:
                return 0
            
            left = helper(root.left, max_height)
            right = helper(root.right, max_height)
            max_height[0] = max(max_height[0], left + right)
            return 1 + max(left, right)
        
        max_height = [0]
        helper(root, max_height)
        return max_height[0]