class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)

        ans = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i] != nums[i-1]:
                ans += len(nums) - i

        return ans


        