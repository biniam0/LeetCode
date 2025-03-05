class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        grid_new = [[0]*c for _ in range(r)]
        
        for i in range(r):
            cur_max = 0
            for j in range(c):
                cur_max = max(cur_max, grid[i][j])
            for j in range(c):
                grid_new[i][j] = cur_max
            
        for j in range(c):
            cur_max = 0
            for i in range(r):
                cur_max = max(cur_max, grid[i][j])
            for i in range(r):
                grid_new[i][j] = min(cur_max, grid_new[i][j])

        ans = 0
        for i in range(r):
            for j in range(c):
                ans += abs(grid_new[i][j] - grid[i][j])

        return ans

        
        


        
