class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binary_search(l, r):
            if l == r:
                return nums[l]
            m = l + (r-l)//2
            if nums[m] < nums[r]:
                return binary_search(l, m)
            else:
                return binary_search(m+1, r)
        return binary_search(0, len(nums)-1)