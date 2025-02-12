class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(sqrt(c))+1
        while l <= r:
            if l**2 + r**2 < c:
                l += 1
            elif l**2 + r**2 > c:
                r -= 1
            elif l**2 + r**2 == c:
                return True
        return False