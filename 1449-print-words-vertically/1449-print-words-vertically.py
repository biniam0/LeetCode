class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        n = len(words)
        mx_word = len(max(words, key=lambda word: len(word)))

        for i in range(n):
            if len(words[i]) < mx_word:
                words[i] = words[i].ljust(mx_word, " ")

        ans = []

        j = 0
        while j < mx_word:
            tmp = ""
            for i in range(len(words)):
                tmp += words[i][j]

            ans.append(tmp)
            j += 1

        ans = [word.rstrip() for word in ans]
        return ans