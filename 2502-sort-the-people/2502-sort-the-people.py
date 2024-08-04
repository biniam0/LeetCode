class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        combined = list(zip(heights, names))

        combined.sort(key=lambda x: x[0], reverse=True)

        sorted_names = [name for height, name in combined]
        return sorted_names