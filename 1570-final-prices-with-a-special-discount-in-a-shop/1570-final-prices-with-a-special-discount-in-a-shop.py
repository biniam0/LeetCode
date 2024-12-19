class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Monotonic Stack O(n)
        res = prices.copy()
        stack = []

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                res[j] -= prices[i]
            stack.append(i)
            res[i] = prices[stack[-1]]

        return res
        # Brute force
        # n = len(prices)
        # res = []

        # for i in range(n):
        #     for j in range(i+1, n):
        #         if prices[i] >= prices[j]:
        #             res.append(prices[i]-prices[j])
        #             break
        #     else:
        #         res.append(prices[i])
        # return res