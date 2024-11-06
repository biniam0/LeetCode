class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        
        for i in range(n):
            flag = False
            for j in range(n-i-1):
                if nums[j] <= nums[j+1]:
                    continue
                if bin(nums[j]).count("1") == bin(nums[j+1]).count("1"):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    flag = True
                else:
                    return False
            if not flag:
                return True
        return True