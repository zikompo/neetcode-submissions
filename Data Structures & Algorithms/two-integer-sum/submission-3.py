class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            dif = target-n
            if dif in d:
                return [d[dif], i]
            d[n] = i

