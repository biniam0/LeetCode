class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles = sorted(piles)
        total = 0
        for i in range(len(piles)//3, len(piles), 2):
            total += piles[i]

        return total
            