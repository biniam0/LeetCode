class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for sell in prices:
            if sell < buy:
                buy = sell
            elif sell - buy > max_profit:
                max_profit = sell - buy
        return max_profit

        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         max_profit = max(max_profit, prices[r] - prices[l])
        #     else:
        #         l += 1
        #     if prices[r] < prices[l]:
        #         l = r
        #     r += 1
        # return max_profit