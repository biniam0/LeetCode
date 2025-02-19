class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0]*(len(s) + 1)
        for i, j, drx in shifts:
            if drx:
                prefix[i] += 1
                prefix[j+1] -= 1
            else:
                prefix[i] -= 1
                prefix[j+1] += 1

        for i in range(1, len(prefix)):
            prefix[i] = prefix[i] + prefix[i-1]

        ans = ""
        for i in range(len(s)):
            tmp = ord(s[i]) + prefix[i]
            if tmp > 122:
                tmp = 97 + (tmp - 123) % 26
            elif tmp < 97:
                tmp = 122 - (96 - tmp) % 26
            ans += chr(tmp)

        return ans