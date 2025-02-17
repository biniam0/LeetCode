class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = Counter()
        prefix_sum[0] = 1
        cur_sum = 0
        ans = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            diff = cur_sum - k
            ans += prefix_sum[diff]
            prefix_sum[cur_sum] = 1 + prefix_sum[cur_sum]
            
        return ans
                