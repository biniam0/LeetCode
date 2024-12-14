class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx_map = {}
        res = [-1]*len(nums1)

        for i in range(len(nums1)):
            idx_map[nums1[i]] = i

        for i in range(len(nums2)):
            if nums2[i] in idx_map:
                for j in range(i+1, len(nums2)):
                    if nums2[i] < nums2[j]:
                        res[idx_map[nums2[i]]] = nums2[j]
                        break

        return res