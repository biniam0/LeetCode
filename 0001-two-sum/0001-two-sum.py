class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_idx = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict_idx:
                return [dict_idx[complement], i]
            dict_idx[nums[i]] = i
            
        return []

        