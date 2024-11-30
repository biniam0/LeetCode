class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_g = []
        n = len(nums2)

        for i in range(n):
            j = i+1
            while j < len(nums2):
                if nums2[i] < nums2[j]:
                    break
                j += 1
            next_g.append(nums2[j] if j < n else -1)

        res = []

        for i in range(len(nums1)):
            idx = nums2.index(nums1[i])
            res.append(next_g[idx])

        return res
