class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_idx = sorted([[num, i]
                      for i, num in enumerate(nums)], key=lambda item: item[0])
        l, r = 0, len(nums)-1

        while l < r:
            if nums_idx[l][0] + nums_idx[r][0] > target:
                r -= 1
            elif nums_idx[l][0] + nums_idx[r][0] < target:
                l += 1
            else:
                return [nums_idx[l][1], nums_idx[r][1]]

