from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()

        def isValid(r, c):
            return 0<=r<rows and 0<=c<cols and grid[r][c] == "1"
        
        islands = 0
        def dfs(r, c):
            for dr, dc in directions:
                if isValid(r+dr, c+dc):
                    grid[r+dr][c+dc] = "0"
                    dfs(r+dr, c+dc)
    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        
        return islands
                
            