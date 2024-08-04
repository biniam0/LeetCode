class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        coverage = [False] * (right - left + 1)
        j = 0
        for i in range(left, right+1):
            for x, y in ranges:
                if (x <= i <= y):
                    coverage[j] = True
            j += 1
        return all(coverage)