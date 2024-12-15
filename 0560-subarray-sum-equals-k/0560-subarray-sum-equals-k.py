class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        cur_sum = 0
        ans = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            diff = cur_sum - k
            if diff in prefix:
                ans += prefix[diff]
            if cur_sum in prefix:
                prefix[cur_sum] += 1
            else:
                prefix[cur_sum] = 1
        return ans