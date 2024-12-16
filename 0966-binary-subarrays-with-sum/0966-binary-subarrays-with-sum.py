class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)

        def helper(x):
            """
                count num of subarrays where curSum <= x
            """
            if x < 0:
                return 0

            res = 0
            l = cur = 0
            for r in range(n):
                cur += nums[r]

                while cur > x:
                    cur -= nums[l]
                    l += 1
                res += (r-l+1)
            return res

        return helper(goal) - helper(goal-1)