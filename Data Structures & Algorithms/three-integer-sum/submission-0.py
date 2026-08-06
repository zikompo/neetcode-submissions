class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst = []
        nums.sort()
        # three indexes. l, r, and one going through the array.
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[i]+nums[l]+nums[r] > 0:
                    r -= 1
                elif nums[i]+nums[l]+nums[r] < 0:
                    l += 1
                else:
                    is_dup = False
                    to_add = [nums[i], nums[l], nums[r]]
                    for l1 in lst:
                        if set(l1) == set(to_add):
                            is_dup = True
                    if not is_dup:
                        lst.append(to_add)
                    l += 1
                    r -= 1
                
        return lst
                    