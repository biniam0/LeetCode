class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s_strs = sorted(strs)
        ans = ""
        first = s_strs[0]
        last = s_strs[-1]

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans