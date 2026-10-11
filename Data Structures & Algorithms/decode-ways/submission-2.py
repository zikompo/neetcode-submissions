class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}

        def ways(i):
            if i == len(s):
                return 1

            if s[i] == "0":
                return 0

            if i in memo:
                return memo[i]

            result = ways(i + 1)

            if i + 1 < len(s) and 10 <= int(s[i:i + 2]) <= 26:
                result += ways(i + 2)

            memo[i] = result
            return result

        return ways(0)
