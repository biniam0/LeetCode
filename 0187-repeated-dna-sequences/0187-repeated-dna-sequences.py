class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        count = Counter()

        l = 0
        for r in range(9,len(s)):
            substring = s[l:r+1]
            count[substring] += 1
            l += 1

        res = []
        for sub in count:
            if count[sub] > 1:
                res.append(sub)

        return res
