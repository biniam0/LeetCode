class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h, n = 0, len(citations)
    
        for i in range(n-1, -1, -1):
            if n-i <= citations[i]:
                h += 1
            else:
                break
        return h
