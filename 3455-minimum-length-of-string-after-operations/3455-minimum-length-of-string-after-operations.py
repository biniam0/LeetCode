class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) < 3:
            return len(s)

        total = 0
        freq = Counter(s)
        for f in freq.values():
            if f >= 3:
                if f % 2 == 1:
                    total += 1
                else:
                    total += 2
            else:
                total += f

        return total

