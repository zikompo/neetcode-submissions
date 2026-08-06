class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        maxAbs = float('-inf')
        minHeap = [(0, (0, 0))] # takes no effort for first one
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        while minHeap:
            effort, coord = heapq.heappop(minHeap)
            if coord in visited:
                continue
            row, col = coord
            if row == rows-1 and col == cols-1:
                return effort
            visited.add(coord)
            for dr, dc in directions:
                r, c = row+dr, col+dc
                if (r in range(rows) and c in range(cols) and (r, c) not in visited):
                    absolute = abs(heights[row][col]-heights[r][c])
                    heapq.heappush(minHeap, (max(absolute, effort), (r, c)))
        
