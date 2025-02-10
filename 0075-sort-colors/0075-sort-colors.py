class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for l in range(len(nums)):
            for r in range(l+1, len(nums)):
                if nums[l] > nums[r]:
                    nums[l], nums[r] = nums[r], nums[l]
                