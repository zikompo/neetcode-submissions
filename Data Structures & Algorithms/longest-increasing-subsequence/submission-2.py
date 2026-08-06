class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [1] * len(nums)
        parents = [-1] * len(nums)
        for i in range(1, len(nums)):
            subproblems = [(cache[k], k) for k in range(i) if nums[k] < nums[i]]
            best_len, best_parent_id = max(subproblems, default=(0, -1))

            cache[i] = 1+best_len
            parents[i] = best_parent_id
        j = len(parents)-1
        lst = []
        while j >= 0:
            lst.append(nums[j])
            j = parents[j]
        print(lst[::-1])
        return max(max(cache), 1)