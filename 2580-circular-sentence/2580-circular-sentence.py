class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        
        sent = sentence.split()

        for i in range(len(sent)-1):
            if sent[i][-1] != sent[i+1][0]:
                return False

        return True