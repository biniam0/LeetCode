class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        m = len(p)
        p_count = Counter(p)
        s_count = Counter()

        l = 0
        for r in range(len(s)):
            s_count[s[r]] += 1

            if r >= m:
                s_count[s[l]] -= 1
                if s_count[s[l]] == 0:
                    del s_count[s[l]]
                l += 1
            if s_count == p_count:
                res.append(l)

        return res