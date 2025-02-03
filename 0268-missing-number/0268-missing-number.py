class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mx = max(nums)+1

        for i in range(mx+1):
            if i not in set(nums):
                return i