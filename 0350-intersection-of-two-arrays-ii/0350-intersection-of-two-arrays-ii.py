class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num_dict = Counter(nums1)

        res = []
        for num in nums2:
            if num in num_dict and num_dict[num] > 0:
                res.append(num)
                num_dict[num] -= 1

        return res
                