class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        for num in nums:
            for t in range(num, target+1):
                prev = dp[t-num]
                for comb in prev:
                    c = comb+[num]
                    dp[t].append(c)
        return dp[target]
                     