class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_sum = 0
        min_size = float("inf")
        if sum(nums) < target:
            return 0
        l = 0
        for r in range(len(nums)):
            cur_sum += nums[r]

            while cur_sum >= target:
                cur_sum -= nums[l]
                min_size = min(min_size, (r-l+1))
                l += 1

        return min_size