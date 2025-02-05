class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        ans = []

        for word in words:
            if set(word.lower()).issubset(row1) or set(word.lower()).issubset(row2) or set(word.lower()).issubset(row3):
                ans.append(word)

        return ans
