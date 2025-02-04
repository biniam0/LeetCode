class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        ans = 0

        for char, freq in s_count.items():
            if freq > t_count[char]:
                ans += (freq - t_count[char])
        return ans