class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i] == val:
                nums[i] = "_"
                count += 1
        count = len(nums) - count
        l = 0
        r = n - 1
        while l < r:
            if nums[l] == "_":
                if nums[r] != "_":
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
                else:
                    r -= 1
            else:
                l += 1
        return count

        