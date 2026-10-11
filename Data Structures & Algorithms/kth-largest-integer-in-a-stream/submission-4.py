import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.largest = nums
        heapq.heapify(self.largest)
        self.k = k
        while len(self.largest) > k:
            heapq.heappop(self.largest)

    def add(self, val: int) -> int:
        heapq.heappush(self.largest, val)
        if len(self.largest) > self.k:
            heapq.heappop(self.largest)
        
        return self.largest[0]