class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {")": "(", "]": "[", "}": "{"}

        stack = []
        for char in s:
            if char in set("([{"):
                stack.append(char)
            elif stack and stack[-1] == bracket_dict[char]:
                stack.pop()
            else:
                return False

        return True if not stack else False
