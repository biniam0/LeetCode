class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l = 0
        for r in range(1, len(nums)):
            nums[r] = nums[l] + nums[r]
            l += 1
        return nums