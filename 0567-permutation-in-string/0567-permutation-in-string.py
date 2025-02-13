class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        s1_freq, s2_freq = Counter(s1), Counter()
        l = 0
        for r in range(m):
            s2_freq[s2[r]] += 1
            if r-l+1 > n:
                s2_freq[s2[l]] -= 1
                if s2_freq[s2[l]] == 0:
                    del s2_freq[s2[l]]
                l += 1
            if s1_freq == s2_freq:
                return True
        return False
