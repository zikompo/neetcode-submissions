class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ""
        for word in strs:
            r+=str(len(word))
            r+= '#'
            r+=word
        print(r)
        return r
    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        while i < len(s):
            i1 = 0
            mini_s = ""
            while i+i1 < len(s) and s[i+i1] != '#':
                mini_s += s[i+i1]
                i1 += 1
            i += i1
            l = int(mini_s)
            i += 1
            lst.append(s[i:i+l])
            i += l
        return lst