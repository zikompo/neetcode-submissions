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
    def evalRPN(self, tokens: List[str]) -> int:
        s = Stack()
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                x = int(s.pop()) #pop the first value
                y = int(s.pop()) #pop the second value
                # remember that y is the older value
                if token == '+':
                    s.push(y+x)
                elif token == '-':
                    s.push(y-x)
                elif token == '*':
                    s.push(x*y)
                else:
                    s.push(int(y/x)) #always truncates towards 0
            else:
                s.push(token)
        return int(s.peek())
                
            