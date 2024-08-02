class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        sorted_nums = sorted(nums)
        num_dict = {}
        for idx, num in enumerate(sorted_nums):
            if num not in num_dict:
                num_dict[num] = idx

        result = [num_dict[num] for num in nums]
        return result