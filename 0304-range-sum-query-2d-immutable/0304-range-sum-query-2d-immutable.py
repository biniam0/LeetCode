class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix_matrix = [[0]*(cols+1) for r in range(rows+1)]
        for i in range(rows):
            prefix = 0
            for j in range(cols):
                prefix += matrix[i][j]
                above = self.prefix_matrix[i][j+1]
                self.prefix_matrix[i+1][j+1] = prefix + above
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        br = self.prefix_matrix[row2+1][col2+1]
        above = self.prefix_matrix[row1][col2+1]
        left = self.prefix_matrix[row2+1][col1]
        topleft = self.prefix_matrix[row1][col1]
        return br - above - left + topleft
