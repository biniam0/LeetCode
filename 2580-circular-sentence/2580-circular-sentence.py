class Solution:
    def isCircularSentence(self, sentence: str) -> bool:    
        for i in range(len(sentence)):
            if sentence[i] == " " and sentence[i-1] != sentence[i+1]:
                return False
        return sentence[0] == sentence[-1]


        # sent = sentence.split()

        # for i in range(len(sent)-1):
        #     if sent[i-1][-1] != sent[i][0]:
        #         return False

        # return True