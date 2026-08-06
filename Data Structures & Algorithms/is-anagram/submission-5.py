class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash1 = {}
        hash2 = {}
        for i in range(len(s)):
            hash1.setdefault(s[i], 0)
            hash1[s[i]] += 1
        for i in range(len(t)):
            hash2.setdefault(t[i], 0)
            hash2[t[i]] += 1 
        for key in hash1:
            if key not in hash2 or hash2[key] != hash1[key]:
                return False
        return True