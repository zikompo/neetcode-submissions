class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Very similar to number of islands, but dfs will have an extra area variable
        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(r, c) -> int:
            if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                area += dfs(r+dr, c+dc)

            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea
            
