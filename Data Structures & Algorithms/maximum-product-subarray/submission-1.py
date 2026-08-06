class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cache = ['a'] * len(nums)
        curr_min = curr_max = ans = nums[0]

        for num in nums[1:]:
            if num < 0:
                curr_min, curr_max = curr_max, curr_min
            curr_min = min(num, curr_min * num)
            curr_max = max(num, curr_max * num)

            ans = max(ans, curr_max)
        return ans