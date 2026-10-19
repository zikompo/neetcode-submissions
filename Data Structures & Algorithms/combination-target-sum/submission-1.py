class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, n = [], []

        def bt(start, currSum):
            if currSum > target:
                return 
            if currSum == target:
                res.append(n[:])
                return
            for i in range(start, len(nums)):
                n.append(nums[i])
                currSum += nums[i]
                bt(i, currSum)               
                currSum -= n.pop()
        
        bt(0, 0)
        return res

            
            
                     