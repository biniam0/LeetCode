class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = i = 0
       
        for i in range(1, len(nums), 2):
            ans += min(nums[i-1], nums[i])

        return ans
