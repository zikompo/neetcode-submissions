class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currSum = currSum1 = 0
        maxSum = minSum = nums[0]
        totalSum = 0 # for wrap around
        # Get maximum regular subarray
        for num in nums:
            totalSum += num
            currSum = max(currSum, 0)
            currSum1 = min(currSum1, 0)
            currSum += num
            currSum1 += num
            maxSum = max(maxSum, currSum)
            minSum = min(minSum, currSum1)

        
        if minSum == totalSum:
            return maxSum
        return max(maxSum, totalSum-minSum)