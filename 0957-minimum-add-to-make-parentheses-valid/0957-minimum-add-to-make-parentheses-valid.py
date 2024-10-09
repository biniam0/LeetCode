class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            # if s[i] == "(":
            if stack and s[i] == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(s[i])
            
            
        return len(stack)