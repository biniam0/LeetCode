class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        l_sum = cnt = 0
        for i in range(len(nums)-1):
            l_sum += nums[i]
            if l_sum >= total-l_sum:
                cnt += 1
        return cnt