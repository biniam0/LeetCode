class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        i, j = 0, 0
        ans = []
        up = True
        while len(ans) != n*m:
            if up:
                while i >= 0 and j < m:
                    ans.append(mat[i][j])
                    i -= 1
                    j += 1
                if j == m:
                    i += 2
                    j -= 1
                else:
                    i += 1
                up = False
            else:
                while i < n and j >= 0:
                    ans.append(mat[i][j])
                    i += 1
                    j -= 1
                if i == n:
                    i -= 1
                    j += 2
                else:
                    j += 1
                up = True
        return ans