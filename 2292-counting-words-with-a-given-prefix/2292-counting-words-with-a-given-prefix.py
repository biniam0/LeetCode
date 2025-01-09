class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for word in words:
            tmp = len(pref)
            if pref == word[:tmp]:
                res += 1
                

        return res