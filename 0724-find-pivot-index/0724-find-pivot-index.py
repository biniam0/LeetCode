class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        left = 0
        for i in range(len(nums)):
            tot -= nums[i]
            if tot == left:
                return i
            left += nums[i]
        return -1