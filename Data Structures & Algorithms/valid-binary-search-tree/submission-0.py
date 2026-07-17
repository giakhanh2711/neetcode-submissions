# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, pMin, pMax):
            if not node:
                return True
            
            if (node.right and node.right.val <= node.val) or \
                (node.left and node.left.val >= node.val) or \
                (node.val <= pMin or node.val >= pMax):
                return False
            
            if pMin < node.val < pMax:
                if dfs(node.left, pMin, node.val):
                    return dfs(node.right, node.val, pMax)

            return False

        return dfs(root, float('-inf'), float('inf')) 