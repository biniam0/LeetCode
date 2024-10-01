class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]

        for price in prices[1:]:
            if price < buy:
                buy = price
            elif price - buy > max_profit:
                max_profit = price - buy

        return max_profit
        # l, r = 0, 1
        # max_profit = 0

        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         max_profit = max(max_profit, prices[r] - prices[l])
        #     else:
        #         l += 1
        #     if prices[r] < prices[l]:
        #         l = r
        #     r += 1
        # return max_profit