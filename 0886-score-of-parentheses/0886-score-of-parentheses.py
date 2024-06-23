class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        bal, ans = 0, 0

        for i in range(len(s)):
            if s[i] == "(":
                bal += 1
            else:
                bal -= 1
                if s[i-1] == "(":
                    ans += 2**bal

        return ans