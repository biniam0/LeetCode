from collections import Counter
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        arr1_dict = Counter(arr1)
        res = []
        for num in arr2:
            rep = arr1_dict[num]
            res.extend([num]*rep)
            del arr1_dict[num]

        for num in sorted(arr1_dict.keys()):
            res.extend([num]*arr1_dict[num])

        return res