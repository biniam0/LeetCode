class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums + nums + nums
        res = [0 for i in range(n)]

        for i in range(n, 2*n):
            if nums[i] > 0:
                mod = (nums[i] % n)
                res[i-n] = nums[mod + i]
            elif nums[i] < 0:
                mod = (abs(nums[i]) % n)
                res[i-n] = nums[i - mod]
            else:
                res[i-n] = nums[i]

        return res