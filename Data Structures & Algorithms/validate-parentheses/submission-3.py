class Stack:
        def __init__(self):
            self.stack = []
        def push(self, item):
            self.stack.append(item)
        def pop(self):
            self.stack.pop()
        def peek(self):
            return self.stack[-1]
class Solution:
    def isValid(self, s: str) -> bool:
        openings = ['(', '[', '{']
        closings = [')', ']', '}']
        stack = Stack()
        for c in s:
            if c in openings:
                stack.push(c)
            if c in closings:
                index = closings.index(c)    
                if stack.stack and stack.peek() == openings[index]:
                    stack.pop()
                else:
                    return False
        if stack.stack:
            return False
        return True
