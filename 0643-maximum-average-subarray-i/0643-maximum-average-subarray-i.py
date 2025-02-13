class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg, tot, l = float("-inf"), 0, 0
        for i in range(len(nums)):
            tot += nums[i]
            if (i-l+1) >= k:
                avg = max(avg, tot/k)
                tot -= nums[l]
                l += 1
        return avg

