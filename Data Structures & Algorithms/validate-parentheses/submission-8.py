class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ("[", "{", "(")
        closing = ("]", "}", ")")
        for char in s:
            if char in opening:
                stack.append(char)
            elif char in closing:
                c_index = closing.index(char)
                if not stack or stack[-1] != opening[c_index]:
                    return False
                stack.pop()
        if stack:
            return False
        return True
