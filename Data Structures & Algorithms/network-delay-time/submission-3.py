import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for source, target, time in times:
            adj[source].append((time, target))
        
        minHeap = [(0, k)]
        shortest = {}

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in shortest:
                continue
            shortest[node] = time

            for t, nei in adj[node]:
                if nei not in shortest:
                    heapq.heappush(minHeap, (time + t, nei))
        
        return max(shortest.values()) if len(shortest) == n else -1


            
