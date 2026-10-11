# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # doens't seem that crazy. 
        # level order traversal with a twist?
        if not root:
            return []
        # how do you know what's on the right?
        # we know at each level, anything at the rightmost point is visible.
        # oh makes sense. 
        queue = deque([root])
        ret = []
        while queue:
            length = len(queue)
            for i in range(len(queue)):
                node = queue.popleft()
                if i == length-1:
                    ret.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ret
