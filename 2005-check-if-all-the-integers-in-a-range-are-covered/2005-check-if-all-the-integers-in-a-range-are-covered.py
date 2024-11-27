class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        for start, end in ranges:
            if start <= left <= end:
                left = end + 1
                
            if left > right:
                return True
        return False