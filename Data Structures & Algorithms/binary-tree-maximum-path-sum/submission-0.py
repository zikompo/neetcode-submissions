# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # I'm thinking DFS with something extra returned
        res = root.val

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left = max(dfs(node.left), 0)    # drop negative branches
            right = max(dfs(node.right), 0)

            res = max(res, node.val + left + right)   # fork: update answer only
            return node.val + max(left, right)        # one branch: return upward

        dfs(root)
        return res
        
