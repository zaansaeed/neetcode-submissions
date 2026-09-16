# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
    
        def traverse(node):
            if not node:
                return
            traverse(node.left)       # 1. Left
            result.append(node.val)   # 2. Root
            traverse(node.right)      # 3. Right

        traverse(root)

        return result[k-1]