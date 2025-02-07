class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k%5 == 0:
            return -1

        remainder = 1%k
        count = 1
        while remainder:
            tmp = remainder*10+1
            remainder = tmp%k
            count += 1

        if remainder == 0:
            return count
        else:
            return -1