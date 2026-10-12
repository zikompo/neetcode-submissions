class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we can replace any character
        counts = defaultdict(int)
        best = 0
        l = 0
        for r in range(len(s)):
            c = s[r]
            counts[c] += 1
            while (r-l+1)-max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            best = max(best, r-l+1)
        return best