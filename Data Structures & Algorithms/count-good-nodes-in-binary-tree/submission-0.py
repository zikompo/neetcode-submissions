# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # since we are looking at paths, probably dfs
        # modified dfs where we return max value seen above
        acc = 0
        def dfs(root, maxNum):
            nonlocal acc
            if root.val >= maxNum:
                acc += 1
            if root.left:
                dfs(root.left, max(root.val, maxNum))
            if root.right:
                dfs(root.right, max(root.val, maxNum))
        dfs(root, -101) # using constraints here
        return acc