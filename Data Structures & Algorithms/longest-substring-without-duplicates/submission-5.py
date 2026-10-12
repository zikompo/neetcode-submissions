class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we have a tracker dict
        # we would also have a variable tracking the length
        if not s:
            return 0

        chars = defaultdict(int)
        l = 0
        maxLength = 0
        for r in range(len(s)):
            c = s[r]
            chars[c] += 1
            while chars[c] > 1:
                chars[s[l]] -= 1
                l += 1
            maxLength = max(maxLength, r-l+1)
        
        return maxLength
                