class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visited = set()
        rows, cols = len(grid), len(grid)
        def bfs(r, c):
            q = deque()
            q.append((r, c, 1))
            visited.add((r, c))
            while q:
                row, col, dist = q.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1]]
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == 0 and (r, c) not in visited):
                        q.append((r, c, dist+1))
                        visited.add((r, c))
                        if r == rows-1 and c == cols-1:
                            return dist+1
            return -1
        if grid[0][0] == 0:
            return bfs(0, 0)
        return -1


