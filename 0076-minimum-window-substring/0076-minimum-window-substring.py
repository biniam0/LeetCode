class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = Counter()
        need = Counter(t)

        pair = [0, 0]
        min_len = float("inf")
        formed = 0
        required = len(need)

        l = 0
        for r in range(len(s)):
            have[s[r]] += 1

            if s[r] in need and have[s[r]] == need[s[r]]:
                formed += 1

            while l <= r and required == formed:
                if min_len > r-l+1:
                    min_len = r-l+1
                    pair = [l, r]

                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    formed -= 1

                l += 1

        return "" if min_len == float("inf") else s[pair[0]:pair[1]+1]