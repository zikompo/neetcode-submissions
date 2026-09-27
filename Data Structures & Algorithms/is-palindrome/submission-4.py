class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = s.replace(" ", "").lower()
        start, end = 0, len(stripped)-1
        while start < end:
            while start < end and not stripped[start].isalnum():
                start += 1
            while start < end and not stripped[end].isalnum():
                end -= 1
            if stripped[start] != stripped[end]:
                return False
            start, end = start + 1, end - 1
        return True
