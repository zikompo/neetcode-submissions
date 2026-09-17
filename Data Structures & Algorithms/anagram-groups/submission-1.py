from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = []
        d = {}
        for string in strs:
            d.setdefault(tuple(sorted(string)), []).append(string)
        for chars in d:
            lst.append(d[chars])
        return lst