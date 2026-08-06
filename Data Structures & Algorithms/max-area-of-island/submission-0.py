class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c, maxArea):
            localArea = 1
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            while q:
                row, col = q.popleft()
                directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if (r in range(rows) and c in range(cols) and (r, c) not in visited and grid[r][c] == 1):
                        visited.add((r, c))
                        q.append((r, c))
                        localArea += 1
            return max(maxArea, localArea)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = bfs(r, c, maxArea)

        return maxArea
