class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # trips doesn't seem to be sorted, we sort it first
        trips.sort(key= lambda item:item[1])

        cap = capacity
        heap = []
        for nP, fr, to in trips:
            while heap and fr >= heap[0][0]:
                cap += heapq.heappop(heap)[1]
            if nP > cap:
                return False
            cap -= nP
            heapq.heappush(heap, (to, nP))
        
        return cap >= 0