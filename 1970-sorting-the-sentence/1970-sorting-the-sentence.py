class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        word_dict = {}

        for word in words:
            idx = word[-1]
            stripped = word.rstrip(idx)
            word_dict[int(idx)] = stripped

        result = []
        for i in range(1, len(word_dict)+1):
            result.append(word_dict[i])

        return " ".join(result)
            