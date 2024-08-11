class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []

        for row in image:
            row.reverse()
            for i in range(len(row)):
                if row[i] == 1:
                    row[i] = 0
                else:
                    row[i] = 1
            result.append(row)

        return result