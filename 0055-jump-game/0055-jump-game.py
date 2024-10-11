class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        n = len(nums)

        for num in nums:
            if gas < 0:
                return False
            elif num > gas: 
                gas = num
            gas -= 1
        return True

        