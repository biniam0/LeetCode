class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cur = pmax = pmin = ans = 0

        for i in range(len(nums)):
            cur += nums[i]
            ans = max(ans, abs(cur - pmax), abs(cur - pmin))

            pmax = max(pmax, cur)
            pmin = min(pmin,  cur)

        return ans

