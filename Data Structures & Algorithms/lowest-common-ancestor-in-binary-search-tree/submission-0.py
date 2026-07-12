# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def helper(root, node, ancestors):
            if not root:
                return False
            
            ancestors.append(root)
            
            if root.val == node.val:
                return True

            if helper(root.left, node, ancestors):
                return True
            if helper(root.right, node, ancestors):
                return True
            ancestors.pop()
            return False
        
        ancestors_p, ancestors_q = [], []
        helper(root, p, ancestors_p)
        helper(root, q, ancestors_q)
        
        p_val = [x.val for x in ancestors_p]
        q_val = [x.val for x in ancestors_q]
        # if len(p_val) < len(q_val):
        #     p_val, q_val = q_val, p_val
        #     ancestors_p, ancestors_q = ancestors_q, ancestors_p
        i = -1
        while True:
            if p_val[i] in q_val:
                return ancestors_p[i]
            i -= 1