class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []

        def bt(start):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                bt(i+1)
                path.pop()
        bt(0)
        return res