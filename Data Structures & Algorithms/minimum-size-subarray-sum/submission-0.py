class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float("inf")
        window = 0
        l = 0
        for r in range(len(nums)):
            window += nums[r]
            while window >= target:
                length = min(length, r-l+1)
                window -= nums[l]
                l += 1
                
        return 0 if length==float("inf") else length