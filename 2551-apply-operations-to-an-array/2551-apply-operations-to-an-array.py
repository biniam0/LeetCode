class Solution(object):
    def applyOperations(self, nums):
        l = 0
        for r in range(1, len(nums)):
            if nums[l] == nums[r]:
                nums[l] = nums[l] * 2
                nums[r] = 0
            l += 1

        result = []
        constant = 0
        for num in nums:
            if num != 0:
                result.append(num)
            else:
                constant += 1

        return result + [0]*constant
            