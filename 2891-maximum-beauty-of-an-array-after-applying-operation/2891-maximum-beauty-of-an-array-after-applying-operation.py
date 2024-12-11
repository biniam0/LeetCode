class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0

        l = 0
        for r in range(len(nums)):
            if nums[r] - nums[l] <= 2*k:
                ans = max(ans, (r-l+1))
            else:
                l += 1

        return ans