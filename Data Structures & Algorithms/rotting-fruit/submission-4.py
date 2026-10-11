from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # seems like another multi bfs question.
        queue = deque()
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        fresh = 0
        def isValid(r, c):
            return 0<=r<rows and 0<=c<cols and grid[r][c] == 1 and (r, c) not in visited
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    if isValid(r+dr, c+dc):
                        queue.append((r+dr, c+dc))
                        visited.add((r+dr, c+dc))
                        fresh -= 1
            minutes += 1
        
        return minutes if fresh == 0 else -1

        