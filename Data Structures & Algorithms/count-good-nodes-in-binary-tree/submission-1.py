# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        acc = 0
        # dfs with a max thing added
        def dfs(node, maxSoFar):
            nonlocal acc
            if not node:
                return
            if node.val >= maxSoFar: 
                acc += 1
            dfs(node.left, max(node.val, maxSoFar))
            dfs(node.right, max(node.val, maxSoFar))
        
        dfs(root, -float('inf'))
        return acc


