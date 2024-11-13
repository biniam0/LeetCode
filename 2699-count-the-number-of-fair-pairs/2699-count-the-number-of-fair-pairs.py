class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def counter(val):
            res, j = 0, len(nums)-1
            for i in range(len(nums)):
                while i < j and nums[i] + nums[j] > val:
                    j -= 1
                res += max(0, j-i)
            return res
        nums.sort()
        result = counter(upper) - counter(lower-1)
        return result