class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total = 0
        remainder_idx = {0:-1}

        for i in range(len(nums)):
            total += nums[i]

            remainder = total%k 
            if remainder in remainder_idx:
                if abs(remainder_idx[remainder] - i) >= 2:
                    return True
            else:
                remainder_idx[remainder] = i
        return False
                