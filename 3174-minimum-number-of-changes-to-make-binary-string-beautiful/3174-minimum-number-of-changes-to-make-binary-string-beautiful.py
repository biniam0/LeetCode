class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        i = 1
        while i < len(s):
            if s[i] != s[i-1]:
                res += 1
            i += 2 
        return res

        l = 0
        res = 0
        for r in range(len(s)):
            if s[l] != s[r]:
                if r%2 == 1:
                    res += 1
                l = r

        return res