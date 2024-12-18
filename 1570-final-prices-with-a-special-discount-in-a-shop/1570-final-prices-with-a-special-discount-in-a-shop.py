class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        res = []

        for i in range(n):
            for j in range(i+1, n):
                if prices[i] >= prices[j]:
                    res.append(prices[i]-prices[j])
                    break
            else:
                res.append(prices[i])
        return res