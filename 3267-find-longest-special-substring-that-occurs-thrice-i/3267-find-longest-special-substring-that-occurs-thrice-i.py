class Solution:
    def maximumLength(self, s: str) -> int:
        s_freq = defaultdict(int)
        ans = -1

        for i in range(len(s)):
            for j in range(i, len(s)):
                s_freq[s[i:j+1]] += 1

        for s, f in s_freq.items():
            if len(set(s)) == 1 and f >= 3:
                ans = max(ans, len(s))

        return ans