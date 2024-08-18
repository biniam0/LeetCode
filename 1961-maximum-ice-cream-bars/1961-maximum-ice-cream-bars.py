class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        counts = 0
        total = 0

        if costs[0] > coins:
            return 0

        for cost in costs:
            total += cost
            if total <= coins:
                counts += 1
            else:
                return counts
            
        return counts
        