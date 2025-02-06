class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sums = []
        cur_even_sum = 0
        idx_even = {}

        for i, num in enumerate(nums):
            if num % 2 == 0:
                cur_even_sum += num
                idx_even[i] = num
        for q in queries:
            val, idx = q
            if idx in idx_even:
                tmp_val = idx_even[idx]
                cur_even_sum -= tmp_val
                del idx_even[idx]
                nums[idx] += val
                if nums[idx] % 2 == 0:
                    idx_even[idx] = nums[idx]
                    cur_even_sum += nums[idx]
            else:
                nums[idx] += val
                if nums[idx] % 2 == 0:
                    idx_even[idx] = nums[idx]
                    cur_even_sum += nums[idx]
            even_sums.append(cur_even_sum)

        return even_sums
