"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
       # could do bfs, use a queue
       # using two queues?
        if not node:
            return
        
        clones = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            curr = queue.popleft()
            for n in curr.neighbors:
                if n not in clones:
                    clones[n] = Node(n.val)
                    queue.append(n)
                clones[curr].neighbors.append(clones[n])

                
        return clones[node]
            
            

