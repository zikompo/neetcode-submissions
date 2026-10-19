class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, paths = [], []
        used = [False] * len(nums)

        def bt():
            if len(paths) == len(nums):
                res.append(paths[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                paths.append(nums[i])
                bt()
                paths.pop()
                used[i] = False

        bt()
        return res
        