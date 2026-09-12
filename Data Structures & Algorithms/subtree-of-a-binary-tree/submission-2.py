# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root, subRoot):
        if root is None:
            return subRoot is None  # subRoot must also be empty to match here
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, a, b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        return (a.val == b.val 
                and self.isSameTree(a.left, b.left) 
                and self.isSameTree(a.right, b.right))