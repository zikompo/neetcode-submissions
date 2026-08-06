class Solution:
    def maxScore(self, s: str) -> int:
        maximum = -1
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            l_count = sum([1 for char in left if char == "0"])
            r_count = sum([1 for char in right if char == "1"])
            maximum = max(maximum, l_count + r_count)
        return maximum