class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            for j in range(i+1, n):
                l, r = j+1, n-1
                while l < r:
                    foursum = nums[i] + nums[j] + nums[l] + nums[r]
                    if foursum == target:
                        sub = [nums[i], nums[j], nums[l], nums[r]]
                        if sub not in res:
                            res.append(sub)
                        l += 1
                        r -= 1
                    elif foursum > target:
                        r -= 1
                    else:
                        l += 1

        return res
