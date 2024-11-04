class Solution:
    def compressedString(self, s: str) -> str:
        n = len(s)
        comp =  ""
        cnt = 0
        l, r = 0, 0

        while r < n:
            cnt = 0
            while r < n and s[l] == s[r] and cnt < 9:
                cnt += 1
                r += 1
            comp += str(cnt) + s[l]
            l = r
        return comp