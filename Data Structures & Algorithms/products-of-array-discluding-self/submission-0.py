class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst1=[]
        p1 = 1
        for num in nums:
            lst1.append(p1)
            p1*=num
        lst2=[0]*len(nums)
        p2=1
        for i in range(len(nums)-1, -1, -1):
            lst2[i] = p2
            p2 *= nums[i]
        l = []
        for i in range(len(nums)):
            l.append(lst1[i]*lst2[i])
        return l


