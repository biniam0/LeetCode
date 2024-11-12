class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        banana_per_hr = r

        while l <= r:
            k = (l+r)//2
            hr = 0

            for pile in piles:
                hr += ceil(pile/k)
            if hr <= h:
                banana_per_hr = min(banana_per_hr, k)
                r = k - 1
            else:
                l = k + 1

        return banana_per_hr
            