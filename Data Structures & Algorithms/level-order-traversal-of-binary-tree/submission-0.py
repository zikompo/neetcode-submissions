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
        lst = []
        queue = [root]
        while queue:
            sublist = []
            l = len(queue)
            for _ in range(len(queue)):
                x = queue.pop(0)
                sublist.append(x.val)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)  
            lst.append(sublist)
        return lst

