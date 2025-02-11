class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        ans, i, tmp = 0, 1, len(piles)//3
        while tmp > 0:
            ans += piles[i]
            i += 2
            tmp -= 1
        return ans
