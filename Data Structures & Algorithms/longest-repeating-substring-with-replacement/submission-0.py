class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res =0
        d = set(s)
        for char in d:
            count = l = 0
            for r in range(len(s)):
                if s[r] == char:
                    count += 1
                while (r-l+1)-count > k:
                    if s[l] == char:
                        count -= 1
                    l += 1
                res = max(res, r-l+1)
        return res