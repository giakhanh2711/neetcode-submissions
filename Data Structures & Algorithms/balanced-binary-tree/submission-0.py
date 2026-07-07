# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True, 0
            
            is_left_true, l_h = dfs(root.left)
            is_right_true, r_h = dfs(root.right)

            if not is_left_true or not is_right_true:
                return False, -1
            
            if abs(l_h - r_h) > 1:
                return False, -1
            
            return True, 1 + max(l_h, r_h)
        

        return dfs(root)[0]