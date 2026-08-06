class Solution:
    def rob(self, nums: List[int]) -> int:
        cache1 = [-1] * (len(nums))
        cache2 = [-1] * (len(nums))
        if len(nums) == 1:
            return nums[0]
        def dfs(i):
            if i >= len(nums)-1:
                return 0
            if cache1[i] != -1:
                return cache1[i]
            cache1[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return cache1[i]
        def dfs2(i):
            if i >= len(nums):
                return 0
            if cache2[i] != -1:
                return cache2[i]
            cache2[i] = max(nums[i] + dfs2(i+2), dfs2(i+1))
            return cache2[i]
        return max(dfs(0), dfs2(1))