from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
    
        prefix = [[0] * (col + 1) for _ in range(row + 1)]

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                prefix[i][j] = (
                    mat[i - 1][j - 1] +
                    prefix[i - 1][j] +
                    prefix[i][j - 1] -
                    prefix[i - 1][j - 1]
                )
        
        ans = [[0] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                r = min(i + k, row - 1)
                c = min(j + k, col - 1)

                rt = max(i - k, 0)
                ct = max(j - k, 0)

                ans[i][j] = (
                    prefix[r + 1][c + 1] -
                    prefix[rt][c + 1] -
                    prefix[r + 1][ct] +
                    prefix[rt][ct]
                )

        return ans
