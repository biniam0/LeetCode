class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start, end = [], []
        for s, e in intervals:
            start.append(s)
            end.append(e)
        start.sort()
        end.sort()

        i, j, res, gr = 0, 0, 0, 0
        while i < len(start) and j < len(end):
            if start[i] <= end[j]:
                gr += 1
                i += 1
            else:
                gr -= 1
                j += 1
            res = max(res, gr)
        return res