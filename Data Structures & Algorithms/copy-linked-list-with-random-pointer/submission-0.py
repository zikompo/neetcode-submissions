"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        randoms = []
        d = {None: None}
        curr = head
        i = 0
        while curr is not None:
            randoms.append(Node(curr.val))
            d[curr] = randoms[i]
            curr = curr.next
            i += 1
           
        i = 0
        curr = head
        while curr is not None:
            randoms[i].next = d[curr.next]
            randoms[i].random = d[curr.random]
            curr = curr.next
            i += 1
        
        return randoms[0]

