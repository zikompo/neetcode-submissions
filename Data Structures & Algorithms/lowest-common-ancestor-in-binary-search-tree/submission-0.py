# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # BST is a clue
        # think it might have to do with checking ranges

        # if root is in range of p and q, return the root
        if min(p.val, q.val) <= root.val <= max(p.val, q.val):
            return root
        # if root is less than min of p and q, recurse down right subtree
        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        # else (if root is more than max of p and q), recurse down left subtree
        else:
            return self.lowestCommonAncestor(root.left, p, q)
        