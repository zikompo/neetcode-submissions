from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window of length s1.
        # quick edge cases are len(s1) > len(s2)
        if len(s1) > len(s2):
            return False
        # s1 has a dict with the counts of chars
        s1counts = Counter(s1)
        s2counts = defaultdict(int)

        l = 0
        for r in range(len(s2)):
            if s1counts == s2counts:
                return True
            s2counts[s2[r]] += 1
            while (r-l+1) > len(s1):
                s2counts[s2[l]] -= 1
                if s2counts[s2[l]] == 0:
                    del s2counts[s2[l]]
                l += 1
        
        return s1counts == s2counts # for case where last element is needed 