class Solution:
    def minimumSteps(self, s: str) -> int:
        rnd, ans = 0, 0
        for i, c in enumerate(s):
            if c == "0":
                ans += (i - rnd)
                rnd += 1
        return ans 
        
        # Two Pointer
        # l = 0
        # ans = 0
        # while s[l] == "0":
        #     l += 1
        # for i, r in enumerate(s, start=l):
        #     if r == "0":
        #         ans += (i-l)
        #         l += 1
        # return ans
