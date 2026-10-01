class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # indices, heights increasing
        best = 0
        for i in range(len(heights) + 1):
            cur = heights[i] if i < len(heights) else 0  # sentinel
            while stack and heights[stack[-1]] > cur:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                best = max(best, h * (i - left - 1))
            stack.append(i)
        return best