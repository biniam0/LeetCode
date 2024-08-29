class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda pair: pair[1])

        if len(points) == 0:
            return 0

        arrow_pos = points[0][1]
        arrow_cnt = 1

        for i in range(1, len(points)):
            if arrow_pos >= points[i][0]:
                continue
            arrow_cnt += 1
            arrow_pos = points[i][1]

        return arrow_cnt