class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return []

        res = Counter(words[0])

        for word in words[1:]:
            current_word = Counter(word)

            res = res & current_word

        return list(res.elements())
                