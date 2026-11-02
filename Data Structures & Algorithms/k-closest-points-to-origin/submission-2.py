import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point1, point2):
            x1, y1 = point1
            x2, y2 = point2
            return ((x1-x2)**2 + (y1-y2)**2)
        
        heap = []
        for point in points:
            heapq.heappush(heap, (distance(point, [0, 0]), point))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res

        