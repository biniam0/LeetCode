class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        m = len(mat)
        n = len(mat[0])

        def transpose(mat):
            t = [[0]*n for _ in range(m)]
        
            for i in range(m):
                for j in range(n):
                    t[j][i] = mat[i][j]

            for i in range(m):
                tmp = t[i]

                l, r = 0, len(tmp)-1
                while l < r:
                    tmp[l], tmp[r] = tmp[r], tmp[l]
                    l += 1
                    r -= 1

                t[i] = tmp
            return t

        if mat == target:
            return True
        else:
            for i in range(3):
                t = transpose(mat)
                if t == target:
                    return True
                else:
                    mat = t
        return False