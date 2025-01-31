class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = float("inf")
        for char in strs:
            if len(char) < min_len:
                min_len = len(char)

        res = ""
        for i in range(min_len):
            temp = strs[0][i]
            for char in strs:
                if char[i] != temp:
                    return res
            res += strs[0][i]
        return res
        


