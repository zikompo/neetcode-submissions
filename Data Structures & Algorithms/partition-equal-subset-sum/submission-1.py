class Solution:
    def canPartition(self, nums: List[int]) -> bool: 
        if sum(nums)%2 != 0:
            return False
        n, m = len(nums), sum(nums)//2
        cache = [[False]*(m+1) for _ in range(n+1)]
        cache[0][0] = True
        for i in range(1, n+1):
            curr_num = nums[i-1]
            for j in range(1, m+1):
                exclude = cache[i-1][j]
                include = False
                if j >= curr_num:
                    include = cache[i-1][j-curr_num]
                cache[i][j] = include or exclude
        return cache[n][m]


