class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        transpose = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                transpose[j][i] = matrix[i][j]

        return transpose
            