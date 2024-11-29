class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        res = 0
        l = 0
        for r in range(2, n):
            if nums[r] - nums[r-1] == nums[r-1] - nums[r-2]:
                res += (r-l-1)
            else:
                l = r -1

        return res


            