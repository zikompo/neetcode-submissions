class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        fresh = set()
        q = deque()
        t = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh.add((r, c))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        if len(q) == 0 and len(fresh) == 0:
            return 0
        # all rotten apples in queue
        while q:
            size = len(q)
            for _ in range(size):
                row, col= q.popleft()
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))
                        grid[r][c] = 2
                        fresh.remove((r, c))
            t += 1
        # no apples should be left
        if len(fresh) == 0:
            return t-1
        return -1
        