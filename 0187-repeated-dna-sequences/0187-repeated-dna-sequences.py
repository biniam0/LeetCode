class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        count = Counter()
        res = set()
        l = 0
        for r in range(9,len(s)):
            substring = s[l:r+1]
            count[substring] += 1

            if substring not in res and count[substring] > 1:
                res.add(substring)
            l += 1
        return list(res)
