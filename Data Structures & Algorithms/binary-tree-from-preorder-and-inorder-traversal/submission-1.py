# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dict_pos = {x:i for i, x in enumerate(inorder)}
        length = len(preorder)
        def helper(s_p, e_p, s_i, e_i):
            if not (0 <= s_p <= e_p) or not (s_p <= e_p < length) or \
                not (0 <= s_i <= e_i) or not (s_i <= e_i < length):
                return None
            
            root_val = preorder[s_p]
            root = TreeNode(root_val)
            root_i = dict_pos[root_val]
            root.left = helper(s_p + 1, s_p + root_i - s_i, s_i, root_i - 1)
            root.right = helper(s_p + root_i - s_i + 1, e_p, root_i + 1, e_i)

            return root
        
        return helper(0, length - 1, 0, length - 1)

        