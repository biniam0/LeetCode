class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jumps = 0
        l = r = 0

        while r < len(nums)-1:
            far = 0
            for i in range(l, r+1):
                far = max(far, i+nums[i])
            l = r+1
            r = far
            min_jumps += 1
        return min_jumps