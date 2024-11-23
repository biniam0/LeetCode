class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # Optimized Solution
        rows, cols = len(box), len(box[0])

        for r in range(rows):
            i = cols - 1
            for c in reversed(range(cols)):
                if box[r][c] == "#":
                    box[r][c], box[r][i] = box[r][i], box[r][c]
                    i -= 1
                elif box[r][c] == "*":
                    i = c - 1

        res = []
        for c in range(cols):
            column = []
            for r in reversed(range(rows)):
                column.append(box[r][c])
            res.append(column)

        return res


        # Time Limit Exceeded(my solution)
        # n = len(box[0])

        # for row in box:
        #     for _ in range(n):
        #         l, r = n-2, n-1
        #         while l >= 0:
        #             if row[l] == "#" and row[r] == ".":
        #                 row[l], row[r] = row[r], row[l]

        #             l -= 1
        #             r -= 1
        # res = zip(*box[::-1])
        # return [list(row) for row in res]