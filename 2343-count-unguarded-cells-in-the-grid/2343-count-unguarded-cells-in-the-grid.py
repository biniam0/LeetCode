class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        tiles = [[0]*n for _ in range(m)]
        # G = guard, W = wall, GD = guardable

        # Marking the Guard and Wall Cells
        for row, col in guards:
            tiles[row][col] = "G"
        for row, col in walls:
            tiles[row][col] = "W"

        def mark_gaurded(r, c):
            # Looking Down
            for row in range(r+1, m):
                if tiles[row][c] in {"W", "G"}:
                    break
                tiles[row][c] = "GD"

            # Looking Up
            for row in range(r-1, -1, -1):
                if tiles[row][c] in {"W", "G"}:
                    break
                tiles[row][c] = "GD"

            # Looking Right
            for col in range(c+1, n):
                if tiles[r][col] in {"W", "G"}:
                    break
                tiles[r][col] = "GD"

            # Looking Left
            for col in range(c-1, -1, -1):
                if tiles[r][col] in {"W", "G"}:
                    break
                tiles[r][col] = "GD"

        for r, c in guards:
            mark_gaurded(r, c)

        return sum(1 for row in tiles for cell in row if cell == 0)
