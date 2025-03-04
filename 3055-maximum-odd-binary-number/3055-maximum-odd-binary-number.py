class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = list(sorted(list(s)))
        return "".join(list(reversed(s[:len(s)-1]))+ list(s[-1]))