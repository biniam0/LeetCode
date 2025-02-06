class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])

        def helper(img, i, j):
            ans = 0
            cells = 0

            # right
            if j+1 < n:
                ans += img[i][j+1]
                cells += 1

            # left
            if j > 0:
                ans += img[i][j-1]
                cells += 1

            # up
            if i > 0:
                ans += img[i-1][j]
                cells += 1

            # down
            if i+1 < m:
                ans += img[i+1][j]
                cells += 1

            # up-left
            if i-1 >= 0 and j > 0:
                ans += img[i-1][j-1]
                cells += 1

            # up-right
            if i-1 >= 0 and j+1 < n:
                ans += img[i-1][j+1]
                cells += 1

            # bottom-left
            if i+1 < m and j > 0:
                ans += img[i+1][j-1]
                cells += 1

            # bottom-right
            if i+1 < m and j+1 < n:
                ans += img[i+1][j+1]
                cells += 1

            ans += img[i][j]
            cells += 1

            return ans, cells

        smoothed_img = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                sum_, cells = helper(img, i, j)
                smoothed_img[i][j] = math.floor((sum_)/(cells))

        return smoothed_img
                    