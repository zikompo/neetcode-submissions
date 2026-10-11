# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashMap = {}
        for i, num in enumerate(inorder):
            hashMap[num] = i
        
        self.pre_idx = 0  # next root to consume from preorder

        def build(left: int, right: int) -> Optional[TreeNode]:
            # left..right is the inorder window for this subtree
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            mid = hashMap[root_val]
            root.left = build(left, mid - 1)    # must go before right
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)
        
        