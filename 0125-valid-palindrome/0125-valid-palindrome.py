class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = set(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
        ans = []
        for i in range(len(s)):
            if s[i] in alphanumeric:
                if s[i].isalpha():
                    ans.append(s[i].lower())
                else:
                    ans.append(s[i])

        ans = "".join(ans)
        l, r = 0, len(ans)-1

        while l <= r:
            if ans[l] != ans[r]:
                return False
            l += 1
            r -= 1

        return True