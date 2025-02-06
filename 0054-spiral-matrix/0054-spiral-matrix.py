class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix:
            if matrix:
                for n in matrix.pop(0):
                    ans.append(n)
            for row in matrix:
                if row:
                    ans.append(row.pop())
            if matrix:
                for n in reversed(matrix.pop()):
                    ans.append(n)
            for i in range(len(matrix)-1, -1, -1):
                if matrix[i]:
                    ans.append(matrix[i].pop(0))

        return ans
            