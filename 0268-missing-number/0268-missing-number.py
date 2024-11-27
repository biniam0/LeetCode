class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums2 = sum(range(0, len(nums)+1))
        return nums2 - sum(nums)
        