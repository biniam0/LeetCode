class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = j = 0

        while i < len(str1) and j < len(str2):
            ord1 = ord(str1[i])
            ord2 = ord(str2[j])
            if ord1 == ord2 or (ord1+1 == ord2) or (ord1 == ord('z') and ord2 == ord("a")):
                j += 1
            i += 1
        
        return j == len(str2)