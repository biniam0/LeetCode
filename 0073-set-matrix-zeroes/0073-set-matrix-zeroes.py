class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        seen_idx = []
        for i in range(m):
            flag = False
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    seen_idx.append(j)
                    flag = True
            if flag == True:
                matrix[i] = [0]*n

        for idx in seen_idx:
            for row in matrix:
                row[idx] = 0