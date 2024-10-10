class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_right = [0]*len(nums)
        max_ = nums[-1]
        for i in range(len(nums)-1, -1, -1):
            max_ = (max(max_, nums[i]))
            max_right[i] = max_
        l, r = 0, 1
        max_width = 0
        while r < len(nums):
            while nums[l] > max_right[r]:
                l += 1
            max_width = max(max_width, r - l)
            r += 1
        return max_width