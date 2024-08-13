class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        unique_nums = sorted(list(set(nums)))
        nums_dict = {}
        for i in range(len(unique_nums)-1, -1, -1):
            nums_dict[unique_nums[i]] = i

        count = 0
        for num in nums:
            count += nums_dict[num]
        return count


        