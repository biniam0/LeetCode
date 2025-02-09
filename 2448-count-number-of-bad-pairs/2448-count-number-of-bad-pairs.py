class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        idx_val = Counter()

        for i in range(n):
            diff = i-nums[i]
            if idx_val[diff] >= 1:
                ans += idx_val[diff]
            idx_val[diff] += 1

        return (n*(n-1))//2 - ans 
        