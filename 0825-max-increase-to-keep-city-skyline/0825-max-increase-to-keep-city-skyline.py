class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        row_max = [0]*r
        col_max = [0]*c

        for i in range(r):
            for j in range(c):
                row_max[i] = max(row_max[i], grid[i][j])
                col_max[j] = max(col_max[j], grid[i][j])
        ans = 0
        for i in range(r):
            for j in range(c):
                tmp = min(row_max[i], col_max[j])
                ans += tmp - grid[i][j]

        return ans

        
        
        
