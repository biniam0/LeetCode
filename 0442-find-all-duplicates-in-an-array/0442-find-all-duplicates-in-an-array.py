class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = set()
        i = 0
        while i < len(nums):
            if nums[i] == nums[nums[i]-1]:
                if i != nums[i]-1:
                    ans.add(nums[i])
                i += 1
            else:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        return list(ans)