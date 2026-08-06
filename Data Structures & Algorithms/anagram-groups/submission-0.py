class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = []
        d = {}
        i = 0
        while i < len(strs):
            alphabet = [0]*26
            for c in strs[i]:
                alphabet[ord(c)-ord('a')] += 1
            d.setdefault(tuple(alphabet), []).append(i)
            i += 1 

        for entry in d:
            lst1 = []
            for i in d[entry]:
                lst1.append(strs[i])
            lst.append(lst1)

        return lst