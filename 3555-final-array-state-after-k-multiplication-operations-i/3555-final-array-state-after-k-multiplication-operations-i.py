class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k > 0:
            min_num = min(nums)
            min_idx = nums.index(min_num)
            nums[min_idx] = min_num * multiplier
            k -= 1
        return nums
