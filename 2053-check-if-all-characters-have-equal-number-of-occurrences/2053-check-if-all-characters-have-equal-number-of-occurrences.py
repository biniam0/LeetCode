class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = list(Counter(s).values())
        tmp = freq[0]
        return all(tmp == n for n in freq)