class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ans = True
        for i in range(left, right+1):
            for s, e in ranges:
                if i in set(range(s, e+1)):
                    break
            else:
                ans = False


        return ans
