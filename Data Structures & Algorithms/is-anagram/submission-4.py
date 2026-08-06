class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for char in s:
            d1.setdefault(char, 0)
            d1[char] += 1
        for char in t:
            d2.setdefault(char, 0)
            d2[char] += 1
        if len(s) != len(t):
            return False
        for char in d1:
            if char not in d2:
                return False
            elif d1[char] != d2[char]:
                return False
        return True
