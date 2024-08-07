class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        flatten_mat = [item for row in mat for item in row]
        reshaped_mat = []

        if r*c != len(flatten_mat):
            return mat
        else:
            for row_idx in range(r):
                reshaped_mat.append(flatten_mat[row_idx*c: row_idx*c+c])
        return reshaped_mat
            