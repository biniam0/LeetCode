class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for b in s:
            if b == "(":
                stack.append(0)
            else:
                val = max(2*stack.pop(), 1)
                stack[-1] += val
        return stack.pop()
            