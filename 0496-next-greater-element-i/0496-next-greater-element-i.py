from collections import defaultdict
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        res = defaultdict(lambda: -1)

        for num in nums2:
            while stack and stack[-1] < num:
                res[stack[-1]] = num
                stack.pop()

            stack.append(num)

        return [res[num] for num in nums1]
      

        
