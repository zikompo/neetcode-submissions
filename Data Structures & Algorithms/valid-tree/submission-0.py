class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adj = {}
        for i in range(n):
            adj[i] = []
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        queue = deque()
        queue.append(0)
        visited = set()
        visited.add(0)
        while queue:
            node = queue.popleft()
            for e in adj[node]:
                if e not in visited:
                    queue.append(e)
                    visited.add(e)
        print(len(visited))
        return len(visited) == n