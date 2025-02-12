class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return 
        l, r = 0, 1

        while r < len(nums):
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
            elif nums[l] != 0 and nums[r] == 0:
                l += 1
                r += 1
            elif nums[l] == 0 and nums[r] == 0:
                r += 1
            elif nums[l] != 0 and nums[r] != 0:
                l += 1
                r += 1
            else:
                r += 1

        
        # BRUTE FORCE
        # n = len(nums)
        # i = n-1
        # while i >= 0:
        #     if nums[i] != 0:
        #         i -= 1
        #         continue
            
        #     idx = i
        #     while idx+1 < n:
        #         nums[idx], nums[idx+1] = nums[idx+1], nums[idx]
        #         idx += 1

        #     i -= 1

        

        