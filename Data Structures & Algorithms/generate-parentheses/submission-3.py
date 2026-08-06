class Stack:
    def __init__(self):
        self.stack = []
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = Stack()

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(s.stack))
                return
            
            if openN < n:
                s.push("(")
                backtrack(openN+1, closedN)
                s.pop()
            
            if closedN < openN:
                s.push(")")
                backtrack(openN, closedN + 1)
                s.pop()

        backtrack(0, 0)
        return res