class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
    
    # Find parent of n, with path compression.
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    # Union by height / rank.
    # Return false if already connected, true otherwise.
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = []
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                edges.append([dist, i, j])
        # should have the edges we need
        for dist, p1, p2 in edges:
            heapq.heappush(minHeap, [dist, p1, p2])
        unionFind = UnionFind(len(points))
        mst = []
        cost = 0
        while len(mst) < len(points)-1:
            dist, p1, p2 = heapq.heappop(minHeap)
            if not unionFind.union(p1, p2):
                continue
            mst.append([p1, p2])
            cost += dist
        return cost

        