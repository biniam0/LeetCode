class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        drx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(i,j):
            if i >= len(grid) or j >= len(grid[0]) \
                or i < 0 or j < 0 or grid[i][j] == 0 :
                return 1

            if (i, j) in visited:
                return 0
            visited.add((i, j))
            ans = 0
            for s, e in drx:
                ans += dfs(i+s, j+e) 
            return ans

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i, j)

        





        