"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        adjList = defaultdict(list)
        q = deque([node])
        seen = {node}
        
        while q:
            node = q.popleft()
            adjList[node.val] = []
            for neighbor in node.neighbors:
                    adjList[node.val].append(neighbor.val)
                    if neighbor not in seen:
                        q.append(neighbor)
                        seen.add(neighbor)
        
        nodes = {k: Node(val = k) for k in adjList.keys()}

        for key, neighbors in adjList.items():
            node = nodes[key]
            for neighbor in neighbors:
                node.neighbors.append(nodes[neighbor])
        
        return nodes[1]

                
                


        