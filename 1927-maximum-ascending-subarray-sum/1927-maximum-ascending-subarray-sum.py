class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur = res = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur += nums[i]
                print(cur)
            else:
                cur = nums[i]
            res = max(res, cur)

        return res