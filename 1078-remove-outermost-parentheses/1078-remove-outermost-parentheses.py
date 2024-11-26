class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        result = []

        for c in s:
            if c == "(":
                if stack:
                    result.append(c)
                stack.append(c)
            else:
                stack.pop()
                if stack:
                    result.append(c)

        return "".join(result)