class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Prefix + Hashmap
        n = len(nums)
        prefix = {0: 1}
        cur_sum = 0
        ans = 0

        for r in range(n):
            cur_sum += nums[r]

            diff = cur_sum - goal
            if diff in prefix:
                ans += prefix[diff]
            
            if cur_sum in prefix:
                prefix[cur_sum] += 1
            else:
                prefix[cur_sum] = 1

        return ans

        # n = len(nums)
        # def helper(x):
        #     """
        #         count num of subarrays where curSum <= x
        #     """
        #     if x < 0:
        #         return 0

        #     res = 0
        #     l = cur = 0
        #     for r in range(n):
        #         cur += nums[r]

        #         while cur > x:
        #             cur -= nums[l]
        #             l += 1
        #         res += (r-l+1)
        #     return res

        # return helper(goal) - helper(goal-1)

        