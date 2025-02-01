class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        mod = full = 0
        res = numBottles
        while numBottles >= numExchange:
            mod = numBottles % numExchange
            full = ((numBottles - mod) // numExchange)
            numBottles = mod + full
            res += full

        return res