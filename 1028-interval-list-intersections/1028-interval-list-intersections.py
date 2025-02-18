class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l, r = 0, 0
        n, m = len(firstList), len(secondList)
        ans = []

        while l < n and r < m:
            if firstList[l][0] <= secondList[r][1] and firstList[l][1] >= secondList[r][0]:
                tmp1 = max(firstList[l][0], secondList[r][0])
                tmp2 = min(firstList[l][1], secondList[r][1])
                print(tmp1, tmp2)
                ans.append([tmp1, tmp2])
            if firstList[l][1] <= secondList[r][1]:
                l += 1
            else:
                r += 1
                
        return ans