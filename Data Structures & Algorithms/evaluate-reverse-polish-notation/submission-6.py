import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        d = {"+": operator.add, "*":operator.mul, "-":operator.sub}
        for token in tokens:
            if token not in ("+", "*", "-", "/"):
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == "/":
                    stack.append(int(num2 / num1))
                else:
                    stack.append(d[token](num2, num1))
        return stack[-1]

