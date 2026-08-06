class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create adjacency list
        adj = {}
        for i in range(1, n+1):
            adj[i] = []

        for source, target, time in times:
            adj[source].append([target, time])

        dist = [float('inf')] * (n+1)
        minHeap = [[0, k]]
        while minHeap:
            time1, node1 = heapq.heappop(minHeap)
            if dist[node1] != float('inf'):
                continue
            dist[node1] = time1
            for node2, time2 in adj[node1]:
                if dist[node2] == float('inf'):
                    heapq.heappush(minHeap, [time1+time2, node2])
        maxTime = 0
        for i in range(1, n+1):
            if dist[i] == float('inf'):
                return -1
            maxTime = max(maxTime, dist[i])
        return maxTime