class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()

        res = float("inf")

        for i in range(n-2):

            l, r = i+1, n-1
            while l < r:
                closest = nums[i]+nums[l]+nums[r]
                if abs(target-closest) < abs(target-res):
                    res = closest

                if closest < target:
                    l += 1
                elif closest > target:
                    r -= 1
                else:
                    return closest

        return res