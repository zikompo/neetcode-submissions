class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [1] * len(nums)
        for i in range(1, len(nums)):
            subproblems = [cache[k] for k in range(i) if nums[k] < nums[i]]
            cache[i] = 1+max(subproblems, default=0)
        return max(max(cache), 1)