class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        tmp_nums = nums
        nums = sorted(nums)
        nums_idx = {}
        for i, num in enumerate(nums):
            if num not in nums_idx:
                nums_idx[num] = i
        res = [nums_idx[num] for num in tmp_nums]
        return res