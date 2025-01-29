class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(map(str, digits))
        return list(map(int, str(int("".join(digits)) + 1)))