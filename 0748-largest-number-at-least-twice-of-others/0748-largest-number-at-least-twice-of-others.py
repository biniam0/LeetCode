class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_idx = nums.index(max(nums))

        for i in range(len(nums)):
            if i != max_idx and nums[i]*2 > nums[max_idx]:
                return -1

        return max_idx
        