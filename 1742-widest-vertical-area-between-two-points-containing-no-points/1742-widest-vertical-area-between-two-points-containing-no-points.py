class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda point: point[0])
        max_width = 0

        for i in range(1, len(points)):
            curr_width = points[i][0] - points[i-1][0]
            max_width = max(max_width, curr_width)

        return max_width
            