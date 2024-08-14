import math
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # Sort points based on their distance from the origin (0, 0)
        points.sort(key=lambda point: point[0]**2 + point[1]**2)

        # Return the first k points
        return points[:k]
                