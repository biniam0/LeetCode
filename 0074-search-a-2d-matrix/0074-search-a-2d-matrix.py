class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix[0]) - 1

        for row in matrix:
            if row[m] >= target:
                if target in row:
                    return True
                else:
                    return False
        