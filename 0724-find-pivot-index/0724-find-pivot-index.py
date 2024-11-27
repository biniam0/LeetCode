class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums) 
        left_sum = 0

        for i, num in enumerate(nums):
            if left_sum == (total_sum - left_sum - num):
                return i
            left_sum += num

        return -1



    #     n = len(nums)
    #     prefix = [0]*n
    #     postfix = [0]*n

    #     for i in range(1, n):
    #         prefix[i] = nums[i-1] + prefix[i-1]

    #     for i in range(n-2, -1, -1):
    #         postfix[i] = nums[i+1] + postfix[i+1]

    #     for i in range(n):
    #         if prefix[i] == postfix[i]:
    #             return i

    #     return -1
