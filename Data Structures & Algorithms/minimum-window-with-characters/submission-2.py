class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        counterT = Counter(t)
        need = len(counterT)
        have = 0

        best = ""
        currD = defaultdict(int)
        l = 0
        for r in range(len(s)):
            c = s[r]
            currD[c] += 1
            if c in counterT and currD[c] == counterT[c]:
                have += 1

            while have == need:
                if not best or r - l + 1 < len(best):
                    best = s[l:r+1]
                currD[s[l]] -= 1
                if s[l] in counterT and currD[s[l]] < counterT[s[l]]:
                    have -= 1
                l += 1

        return best