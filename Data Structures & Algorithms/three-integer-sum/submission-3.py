class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        # [-4, -1, -1, 0, 1, 2]
        ret = []
        a = 0
        while a < len(nums)-2:
            if a > 0 and sorted_nums[a] == sorted_nums[a-1]:
                a += 1
                continue
            b, c = a+1, len(nums)-1           
            target = -sorted_nums[a]
            while b < c:    
                if sorted_nums[b]+sorted_nums[c] == target:
                    ret.append([sorted_nums[a], sorted_nums[b], sorted_nums[c]])
                    b += 1
                    c -= 1
                    while b < c and sorted_nums[b] == sorted_nums[b-1]:
                        b += 1
                    while b < c and sorted_nums[c] == sorted_nums[c+1]:
                        c -= 1
                elif sorted_nums[b]+sorted_nums[c] > target:
                    c -= 1
                else:
                    b += 1
            a += 1
        return ret
