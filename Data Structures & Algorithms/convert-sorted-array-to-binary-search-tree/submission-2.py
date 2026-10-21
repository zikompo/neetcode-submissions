class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def binary_search(l, r, arr):
            if l > r:
                return None
            m = l + (r-l)//2
            root = TreeNode(arr[m])
            root.left = binary_search(l, m-1, arr)
            root.right = binary_search(m+1, r, arr)

            return root
        
        return binary_search(0, len(nums)-1, nums)
