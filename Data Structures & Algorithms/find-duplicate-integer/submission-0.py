class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup = [0]*(len(nums)+1)
        for num in nums:
            if dup[num] != 0:
                return num
            dup[num]-=1
        
