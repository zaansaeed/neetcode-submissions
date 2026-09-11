# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def height(node):
            nonlocal best
            if not node:
                return 0
            l = height(node.left)
            r = height(node.right)
            best = max(best, l + r)   # path bending here, in edges
            return 1 + max(l, r)      # what the parent needs

        height(root)
        return best