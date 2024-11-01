class Solution:
    def makeFancyString(self, s):
        res = []
        for char in s:
            if len(res) < 2 or not (res[-1] == res[-2] == char):
                res.append(char)
        return "".join(res)

        # ans = s[0]
        # cnt = 1

        # for i in range(1, len(s)):
        #     if s[i] == ans[-1]:
        #         cnt += 1
        #         if cnt < 3:
        #             ans += s[i]
        #     else:
        #         cnt = 1
        #         ans += s[i]
        # return ans