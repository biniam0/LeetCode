class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(n):
            l, r = 0, len(nums)
            while l < r:
                mid = (l+r)//2
                if nums[mid] < n:
                    l = mid + 1
                else:
                     r = mid
            return l
        l = binarySearch(target)
        r = binarySearch(target+1)-1
        if l <= r:
            return [l, r]
        return [-1, -1]
