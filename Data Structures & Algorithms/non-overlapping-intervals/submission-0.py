class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removed = 0
        intervals.sort(key=lambda i:i[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            if start < res[-1][1]:
                res[-1][1] = min(end, res[-1][1])
                removed += 1
            else:
                res.append([start, end])
        return removed

[1, 2], [1, 4], [2, 4]