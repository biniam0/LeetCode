class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        if n < 2:
            return 0
        max_diff = float("-inf")

        l = 0
        for r in range(1, n):
            max_diff = max(max_diff, nums[r] - nums[l])
            l += 1

        return max_diff

        