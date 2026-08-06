class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}
        for i in range(n):        
            adj[i] = []
        for i in range(len(edges)):
            a, b = edges[i][0], edges[i][1]
            adj[a].append((b, succProb[i]))
            adj[b].append((a, succProb[i]))
        
        visited = set()
        minHeap = [[-1, start_node]]
        while minHeap:
            sP, edge = heapq.heappop(minHeap)
            if edge in visited:
                continue
            if edge == end_node:
                return -sP
            visited.add(edge)
            
            for e, prob in adj[edge]:
                if e not in visited:
                    heapq.heappush(minHeap, [sP*prob, e])
        return 0
