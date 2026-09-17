from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = Counter(s)
        d2 = Counter(t)

        for char in d1:
            if char not in d2 or d1[char] != d2[char]:
                return False

        return True