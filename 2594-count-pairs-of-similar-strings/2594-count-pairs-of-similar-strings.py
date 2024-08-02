class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if set(words[j]) == set(words[i]):
                    count += 1

        return count
            