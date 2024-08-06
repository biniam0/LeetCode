class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        left, right, n = 0, len(arr)-1, len(arr)

        while left + 1 < n and arr[left] < arr[left+1]:
            left += 1
        while right > 0 and arr[right] < arr[right-1]:
            right -= 1

        return 0 < left == right < n-1