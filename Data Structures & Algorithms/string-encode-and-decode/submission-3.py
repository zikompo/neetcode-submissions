class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for i, string in enumerate(strs):
            ret += str(len(string)) + "#" + string
        print(ret)
        return ret
    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            ret.append(s[i:i+length])
            i += length
        return ret