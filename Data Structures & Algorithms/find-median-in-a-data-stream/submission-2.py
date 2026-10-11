import heapq
class MedianFinder:
    # the way i'm thinking about it, mid value of max/min heap is median
    def __init__(self):
        self.small = [] #max-heap (negated): lower half
        self.large = [] #min-heap, upper half

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        # this is where things may get interesting
        # we have to pop until length is // 2. 
        # if odd, top of stacks will be the same. if even, add two tops and //2
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0]+self.large[0])/2