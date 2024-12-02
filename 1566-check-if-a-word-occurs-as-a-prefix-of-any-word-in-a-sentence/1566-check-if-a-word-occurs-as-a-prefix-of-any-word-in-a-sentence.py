class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        m = len(searchWord)
        for i, char in enumerate(sentence):
            if searchWord[0] == char[0]:
                if searchWord == char[:m]:
                    return i+1

        return -1