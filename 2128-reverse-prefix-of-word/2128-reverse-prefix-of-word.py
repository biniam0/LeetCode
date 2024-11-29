class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if not ch:
            return word

        stack = []

        i = 0
        while i < len(word):
            stack.append(word[i])
            if word[i] == ch:
                break
            i += 1
        if i == len(word):
            return word
        res = ""
        while stack:
            res += stack.pop()
        res += word[i+1:]
        return res