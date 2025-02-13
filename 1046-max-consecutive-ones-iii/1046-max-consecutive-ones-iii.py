class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        zeros = 0
        ans = 0

        l = 0
        r = 0
        while r < n:
            if nums[r] == 0:
                zeros += 1

            while zeros > k and nums[r] == 0:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            ans = max(ans, r-l+1)
            r += 1

        return ans