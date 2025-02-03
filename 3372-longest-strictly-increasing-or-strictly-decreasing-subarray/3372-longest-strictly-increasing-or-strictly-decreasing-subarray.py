class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_incr = 0

        for i in range(len(nums)):
            cur_len = 1
            for j in range(i+1, len(nums)):
                if nums[j-1] < nums[j]:
                    cur_len += 1
                else:
                    break
            max_incr = max(max_incr, cur_len)
        
        for i in range(len(nums)):
            cur_len = 1
            for j in range(i+1, len(nums)):
                if nums[j-1] > nums[j]:
                    cur_len += 1
                else:
                    break
            max_incr = max(max_incr, cur_len)

        return max_incr
