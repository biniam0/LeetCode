class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s_nums = list(set(nums))
        nums_sort = sorted(s_nums)
        if len(nums_sort) < 3:
            return nums_sort[-1]
        return nums_sort[-3]