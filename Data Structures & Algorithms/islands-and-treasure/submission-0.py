class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def treasure_bfs(grid):
            visited = set()
            queue = deque()
            queue.append((0, 0))
            treasure_coords = set()
            while queue:
                r, c = queue.popleft()
                if r in range(ROWS) and c in range(COLS) and (r, c) not in visited:
                    visited.add((r, c))
                    if grid[r][c] == 0 and (r, c) not in treasure_coords:
                        treasure_coords.add((r, c))
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if row in range(ROWS) and col in range(COLS) and (row, col) not in visited:
                        if grid[row][col] != -1:
                            queue.append((row, col))
            return treasure_coords
        treasure_spots = treasure_bfs(grid)
        visited = set()
        queue = deque()
        for t_r, t_c in treasure_spots:
            queue.append((t_r, t_c))
        dist = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = min(grid[r][c], dist)
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if row in range(ROWS) and col in range(COLS):
                        if (row, col) not in visited and (row, col) not in treasure_spots and grid[r][c] != -1:
                            visited.add((row, col))
                            queue.append((row, col))
            dist += 1




        


            
            