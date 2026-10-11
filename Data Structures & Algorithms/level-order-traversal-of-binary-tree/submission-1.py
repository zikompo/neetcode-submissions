# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # level order is BFS, so use a queue
        if not root:
            return []
        queue = deque([root])
        ret = []
        while queue:
            subRet = []
            for i in range(len(queue)):
                node = queue.popleft()
                subRet.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ret.append(subRet)
        return ret

