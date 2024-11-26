class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_depth = 0

        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")" and stack[-1] == "(":
                max_depth = max(len(stack), max_depth)
                stack.pop()

        return max_depth