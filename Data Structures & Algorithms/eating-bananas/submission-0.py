class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxEat = max(piles)
        def can_finish(m):
            hours = 0
            for bananas in piles:
                hours += -(bananas // -m)
            return hours <= h
            
        def binary_search(l, r):
            if l == r:
                return l
            m = l + (r-l)//2
            if can_finish(m):
                return binary_search(l, m)
            else:
                return binary_search(m+1, r)
        
        return binary_search(1, maxEat)