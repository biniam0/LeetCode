class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        if not s:
            return 0
        max_len = float("-inf")
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r]) 
            max_len = max(max_len, r-l+1)
        return max_len