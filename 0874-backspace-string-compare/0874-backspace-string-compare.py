class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(s):
            stack = []
            for char in s:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return ''.join(stack)
        return process_string(s) == process_string(t)