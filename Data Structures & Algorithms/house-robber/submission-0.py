class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        maximum = -1
        def dp(i):
            if i < 0 or i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = max(nums[i]+dp(i+2), dp(i+1))
            return cache[i]
        return dp(0)