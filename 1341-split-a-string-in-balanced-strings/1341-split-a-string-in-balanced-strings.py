class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = s.count("R")
        l = s.count("L")
        i = len(s) - 1
        ans = 0
        while i >= 0:
            if r == l:
                ans += 1

            if s[i] == "R":
                r -= 1
            else:
                l -= 1
            i -= 1
        return ans
