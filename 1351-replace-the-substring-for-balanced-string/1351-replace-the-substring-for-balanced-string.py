class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        freq = Counter(s)
        cn = n // 4
        max_len = float("inf")

        l = 0
        for r in range(n):
            freq[s[r]] -= 1

            while l < n and all(freq[char] <= cn for char in "QWER"):
                max_len = min(r-l+1, max_len)
                freq[s[l]] += 1
                l += 1

        return max_len



        