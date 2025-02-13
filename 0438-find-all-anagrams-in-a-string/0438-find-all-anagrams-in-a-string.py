class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_freq = Counter(p)
        sub_freq = Counter()
        ans = []

        l = 0
        for r in range(len(s)):
            sub_freq[s[r]] += 1

            if r-l+1 > len(p):
                sub_freq[s[l]] -= 1
                l += 1

            if sub_freq == p_freq:
                ans.append(l)

        return ans