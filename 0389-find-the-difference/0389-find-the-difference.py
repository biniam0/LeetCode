class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_freq = Counter(s)
        t_freq = Counter(t)

        for char in t:
            if s_freq[char] != t_freq[char]:
                return char