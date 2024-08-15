class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x_vals = sorted([x for x, y in points])
        max_width = 0

        for i in range(1, len(x_vals)):
            max_width = max(max_width, x_vals[i]-x_vals[i-1])

        return max_width
            