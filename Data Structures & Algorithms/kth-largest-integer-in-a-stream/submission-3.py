class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.lst = []
        self.k = k
        for num in nums:
            heapq.heappush(self.lst, num)
            if len(self.lst) > k:
                heapq.heappop(self.lst)

    def add(self, val: int) -> int:
        heapq.heappush(self.lst, val)
        if len(self.lst) > self.k:
            heapq.heappop(self.lst)
        return self.lst[0]
