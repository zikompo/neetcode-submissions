import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # my first thought is to do somethnig with eucledian distances
        # possibly use a dict to store distances, with key being the distance
        # and the value being a list of points with that distance
        # get a list of the distances, and then heapify and keep only the top k elements.

        def distance(point1, point2):
            x1, y1 = point1
            x2, y2 = point2

            return ((x1-x2)**2 + (y1-y2)**2)**(1/2)
        
        distances = {}
        for point in points:
            d = distance(point, [0, 0])

            if d not in distances:
                distances[d] = []
            distances[d].append(point)
        
        # create the list and then the heap
        lst = [distance for distance in distances]
        heapq.heapify(lst)

        ret = []
        while len(ret) < k:
            d = heapq.heappop(lst)
            ret += distances[d]
        
        return ret[:k] # to deal multiple points with the same distance?
