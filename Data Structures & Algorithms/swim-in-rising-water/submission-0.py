class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minHeap = [[grid[0][0], (0, 0)]]
        visited = set()
        while minHeap:
            time, coord = heapq.heappop(minHeap)
            if coord in visited:
                continue
            if coord == (rows-1, cols-1):
                return time
            visited.add(coord)
            row, col = coord[0], coord[1]
            for dr, dc in directions:
                r, c = row+dr, col+dc
                if (r in range(rows) and c in range(cols) and (r, c) not in visited):
                    heapq.heappush(minHeap, [max(grid[r][c], time), (r, c)])

                
            

