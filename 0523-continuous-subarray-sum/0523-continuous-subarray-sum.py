class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0:-1}
        cur_sum = 0

        for i, num in enumerate(nums):
            cur_sum += num
            r = cur_sum%k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True
        return False