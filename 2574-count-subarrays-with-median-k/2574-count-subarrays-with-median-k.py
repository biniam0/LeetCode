class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pos = nums.index(k)
        rep_count = defaultdict(int)
        bal = 0

        for idx in range(pos, len(nums)):
            bal += int(nums[idx] > k) - int(nums[idx] < k)
            rep_count[bal] += 1

        bal = 0
        ans = 0
        for index in range(pos, -1, -1):
            bal += int(nums[index] > k) - int(nums[index] < k)
            ans += rep_count[-bal]
            ans += rep_count[-bal + 1]

        return ans