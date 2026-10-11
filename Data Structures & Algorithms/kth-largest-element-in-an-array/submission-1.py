import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = nums[:]
        heapq.heapify(n)
        while len(n) > k:
            heapq.heappop(n)
        
        return n[0]
