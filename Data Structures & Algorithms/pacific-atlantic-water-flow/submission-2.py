from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def isValid(r, c):
            return 0<=r<rows and 0<=c<cols

        # we start from the water. If cell has higher height, we go there. 

        pac = set()
        atl = set()

        def dfs(r, c, visited):
            h = heights[r][c]
            visited.add((r, c))
            for dr, dc in directions:
                if isValid(r+dr, c+dc) and (r+dr, c+dc) not in visited and h <= heights[r+dr][c+dc]:
                    dfs(r+dr, c+dc, visited)
    
        for r in range(rows):
            dfs(r, 0, pac)
            dfs(r, cols-1, atl)

        for c in range(cols):
            dfs(0, c, pac)
            dfs(rows-1, c, atl)

        return [[r, c] for r, c in pac & atl]