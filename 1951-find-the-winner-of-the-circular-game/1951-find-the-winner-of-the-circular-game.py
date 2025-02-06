class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [n for n in range(1, n+1)]

        i = 0
        last_stop = 0

        while len(nums) > 1:
            mod = (i+k-1) % len(nums)
            last_stop = mod

            nums.remove(nums[mod])
            i = last_stop

        return nums[0]