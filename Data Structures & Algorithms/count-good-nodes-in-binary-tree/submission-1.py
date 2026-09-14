# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        if root is None:
            return 0
        q = deque([(float('-inf'), root)])

        while q:
            max, node = q.popleft()
            
            if node.val >= max:
                max = node.val
                res += 1

            if node.left:
                q.append([max, node.left])
            if node.right:
                q.append([max, node.right])
        return res
