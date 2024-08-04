class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        res = dict()
        for i in range(len(heights)):
            res[heights[i]] = names[i]

        del names[:]
        height = sorted(res.keys(), reverse=True)

        for i in range(len(heights)):
            names.append(res[height[i]])
        return names