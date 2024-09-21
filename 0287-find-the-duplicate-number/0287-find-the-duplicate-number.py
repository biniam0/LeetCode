class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        r = 1

        for num in nums:
            if num == nums[r] and r < len(nums):
                return (num)
                
            r += 1