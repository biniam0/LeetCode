class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        res = 0
        nums = sorted(nums, reverse=True)

        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                res = max(res, nums[i]+nums[i+1]+nums[i+2])

        return res

