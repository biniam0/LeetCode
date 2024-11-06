class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def count_bits(n):
            return bin(n).count('1')

        cur_min, cur_max = nums[0], nums[0]
        prev_max = float("-inf")

        for n in nums:
            if count_bits(n) == count_bits(cur_min):
                cur_min = min(cur_min, n)
                cur_max = max(cur_max, n)
            else:
                if cur_min < prev_max:
                    return False
                prev_max = cur_max
                cur_min, cur_max = n, n
        if cur_min < prev_max:
            return False
        return True
        # n = len(nums)
        
        # for i in range(n):
        #     flag = False
        #     for j in range(n-i-1):
        #         if nums[j] <= nums[j+1]:
        #             continue
        #         if bin(nums[j]).count("1") == bin(nums[j+1]).count("1"):
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        #             flag = True
        #         else:
        #             return False
        #     if not flag:
        #         return True
        # return True