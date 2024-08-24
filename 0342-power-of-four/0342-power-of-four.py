import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Using Logarithm
        
        return False if n <= 0 else math.log(n, 4) == int(math.log(n, 4))
        # Using Recursion
        # if n == 1: return True
        # if n < 1: return False

        # return self.isPowerOfFour(n/4)