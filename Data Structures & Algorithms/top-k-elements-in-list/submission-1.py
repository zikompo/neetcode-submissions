class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst = []
        d = {}
        for num in nums:
            if num not in d:
                d[num] = nums.count(num)
        lst1 = []
        for num in d:
            lst1.append(d[num])
        lst1.sort()
        lst1 = lst1[-k:]
        for num in lst1:
            for n in d:
                if d[n] == num:
                    lst.append(n)

        return list(set(lst))
