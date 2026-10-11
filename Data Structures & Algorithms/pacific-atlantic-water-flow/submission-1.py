from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # maybe some helpers for checking if we are have reached the atlantic or pacific
        # initially tried bfs, but dfs probably better

        # go uphill bro
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[r][c]):  # climb uphill
                    dfs(nr, nc, visited)

        for c in range(cols):
            dfs(0, c, pac)           # top row touches the Pacific
            dfs(rows - 1, c, atl)    # bottom row touches the Atlantic
        for r in range(rows):
            dfs(r, 0, pac)           # left column touches the Pacific
            dfs(r, cols - 1, atl)    # right column touches the Atlantic

        return [[r, c] for r, c in pac & atl]





