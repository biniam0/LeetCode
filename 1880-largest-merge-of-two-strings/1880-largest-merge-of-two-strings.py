class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = ""
        while i < len(word1) and j < len(word2):
            if word1[i] > word2[j]:
                res += word1[i]
                i += 1
            elif word1[i] < word2[j]:
                res += word2[j]
                j += 1
            else:
                if word1[i:] > word2[j:]:
                    res += word1[i]
                    i += 1
                else:
                    res += word2[j]
                    j += 1
                # temp_i, temp_j = i, j
                # while temp_i < len(word1) and temp_j < len(word2) and word1[temp_i] == word2[temp_j]:
                #     temp_i += 1
                #     temp_j += 1
                
                # if temp_j == len(word2) or (temp_i < len(word1) and word1[temp_i] > word2[temp_j]):
                #     res += word1[i]
                #     i += 1
                # else:
                #     res += word2[j]
                #     j += 1
        return res + word1[i:] + word2[j:]