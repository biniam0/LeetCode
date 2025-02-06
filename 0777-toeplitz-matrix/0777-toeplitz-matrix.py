class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                cur_num = matrix[i][j]
                if i+1 < m and j+1 < n:
                    if cur_num != matrix[i+1][j+1]:
                        return False

        return True