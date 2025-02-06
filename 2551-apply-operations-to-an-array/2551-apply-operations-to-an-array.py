class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        def helper(nums):  
            l = 0
            while l < n:
                if nums[l] == 0:
                    r = l
                    while r < n and nums[r] == 0:
                        r += 1

                    if r < n:
                        nums[l], nums[r] = nums[r], nums[l]
                l += 1
            return nums

        n = len(nums)
        i = 0
        while i <= n-2:
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

            i += 1

        return helper(nums)

    