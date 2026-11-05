class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # trips doesn't seem to be sorted, we sort it first
        trips.sort(key= lambda item:item[1])

        heap = []
        currCapacity = capacity

        for np, fr, to in trips:
            while heap and heap[0][0] <= fr:
                currCapacity += heapq.heappop(heap)[1]
            
            currCapacity -= np
            if currCapacity < 0:
                return False
            
            heapq.heappush(heap, (to, np))
        
        return True

[2]
