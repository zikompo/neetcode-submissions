import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # it is a directed graph
        numNodes = n
        adj = defaultdict(list)
        for src, dst, ti in times:
            adj[src].append((dst, ti))
        
        shortest = set()
        visited = 0
        heap = [(0, k)]
        

        while heap:
            t, n = heapq.heappop(heap)

            if n in shortest:
                continue
            shortest.add(n)
            visited += 1

            if visited == numNodes:
                return t
        
            for nei, t1 in adj[n]:
                if nei not in shortest:
                    heapq.heappush(heap, (t+t1, nei))
        

        return -1


        
            
