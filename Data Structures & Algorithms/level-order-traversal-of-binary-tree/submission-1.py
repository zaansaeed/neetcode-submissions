# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        q = deque([[root, 1]])

        mapper = defaultdict(list)
        while q:
            node, i = q.popleft()
            mapper[i].append(node.val)
            if node.left:
                q.append([node.left, i+1])
            if node.right:
                q.append([node.right, i+1])
        return [val for _, val in mapper.items()]
