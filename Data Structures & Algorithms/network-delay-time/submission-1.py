class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for i in range(1, n+1):
            adj[i] = []

        for src, dst, time in times:
            adj[src].append((dst, time))
        
        minHeap = [(0, k)]
        visited = set()
        while minHeap:
            t, s = heapq.heappop(minHeap)
            if s in visited:
                continue
            visited.add((s))
            if len(visited) == n:
                return t
            for d, ti in adj[s]:
                if d not in visited:
                    heapq.heappush(minHeap, (ti+t, d))
        return -1


            
