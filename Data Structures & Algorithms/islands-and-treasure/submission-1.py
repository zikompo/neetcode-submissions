from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # since it's distance, bfs may be the best method. so we use a queue

        # we will have to go thorugh every treasure first, then do bfs from there
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def isValid(r, c):
            return 0<=r<rows and 0<=c<cols and grid[r][c] == 2147483647

        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                if isValid(r+dr, c+dc):
                    grid[r+dr][c+dc] = grid[r][c] + 1
                    queue.append((r+dr, c+dc))
        




        


            
            