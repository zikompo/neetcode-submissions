class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)

        # using negative probabilities?
        
        for i in range(len(edges)):
            start, end = edges[i]
            prob = succProb[i]
            adj[start].append((prob, end))
            adj[end].append((prob, start))

        maxProb = {}
        maxHeap = [(-1, start_node)]

        while maxHeap:
            prob, node = heapq.heappop(maxHeap)

            if node in maxProb:
                continue
            maxProb[node] = prob

            for p, nei in adj[node]:
                if nei not in maxProb:
                    heapq.heappush(maxHeap, (prob * p, nei)) # prob will go negative here
        if end_node in maxProb:
            return -maxProb[end_node]
        return 0




