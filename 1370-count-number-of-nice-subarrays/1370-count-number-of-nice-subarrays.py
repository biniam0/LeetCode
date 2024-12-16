class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0

        odds = 0
        l = m = 0
        for r in range(n):
            if nums[r] % 2 != 0:
                odds += 1
                
            while odds > k:
                if nums[l] % 2 != 0:
                    odds -= 1
                l += 1
                m = l
            if odds == k:
                while nums[m] % 2 == 0:
                    m += 1
                res += (m-l+1)

        return res
