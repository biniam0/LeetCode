class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) < 3:
            return len(s)

        freq = Counter(s)
        total = 0
        for char in freq.keys():
            total += 2 - (freq[char] % 2)
        return total