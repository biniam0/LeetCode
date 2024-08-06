class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        result = [0]*len(arr)
        max_num = -1
        for i in range(len(arr)-1, -1, -1):
            result[i] = max_num
            max_num = max(arr[i], max_num)
            
        return result
            