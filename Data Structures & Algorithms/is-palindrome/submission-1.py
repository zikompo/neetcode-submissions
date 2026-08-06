class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        new_s = s.replace(" ", "")
        new_s = new_s.lower()
        r = len(new_s)-1
        while l < r:
            if not new_s[l].isalnum():
                l += 1
                continue
            if not new_s[r].isalnum():
                r -= 1
                continue
            if new_s[l] != new_s[r]:
                return False
            l += 1
            r -= 1
        return True