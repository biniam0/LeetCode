class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1+nums2)
        n = len(nums)

        if n%2 != 0:
            return nums[n//2]
        else:
            temp = n//2
            res = (nums[temp] + nums[temp-1])/2
            return res
