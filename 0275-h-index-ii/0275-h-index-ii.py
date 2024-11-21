class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Binary Search Approach
        n = len(citations)
        l, r = 0, n-1
        
        while l <= r:
            mid = (l+r)//2
            if citations[mid] >= n - mid:
                r = mid - 1
            else:
                l = mid + 1
        return n - l

        # Iterative Approach
        # h, n = 0, len(citations)
    
        # for i in range(n-1, -1, -1):
        #     if n-i <= citations[i]:
        #         h += 1
        #     else:
        #         break
        # return h
