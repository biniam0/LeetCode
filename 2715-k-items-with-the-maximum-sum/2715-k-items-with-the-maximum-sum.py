class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        """
            Obj
        """
        if numOnes >= k:
            return k

        if numOnes + numZeros >= k:
            return numOnes

        return numOnes - (k - (numOnes + numZeros))