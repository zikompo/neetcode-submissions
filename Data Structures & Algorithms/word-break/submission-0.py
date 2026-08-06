class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s) : True}
        
        def dfs(i):
            if i in memo:
                return memo[i]
            for word in wordDict:
                if word == s[i:i + len(word)] and (i+len(word) <= len(s)):
                    if dfs(i+len(word)):
                        memo[i] = True
                        return True               
            memo[i] = False
            return False
        return dfs(0)