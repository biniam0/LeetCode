class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0
        for l in range(n):
            count = Counter()
            for r in range(l, n):
                count[s[r]] += 1
                ans += (max(count.values()) - min(count.values()))

        return ans