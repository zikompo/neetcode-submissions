class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        d = set()
        max_l = 0
        for r in range(len(s)):
            while s[r] in d:
                d.remove(s[left])
                left += 1
            d.add(s[r])
            max_l = max(max_l, r-left+1) 
        return max_l