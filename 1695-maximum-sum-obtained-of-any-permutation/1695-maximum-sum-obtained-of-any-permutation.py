class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        count = [0]*(len(nums) + 1)

        for s, e in requests:
            count[s] += 1
            count[e+1] -= 1

        nums.sort(reverse=True)
        count = list(accumulate(count))
        count.sort(reverse=True)
        ans = 0
        for r in range(len(nums)):
            ans += (count[r] * nums[r])
        return ans % MOD
