class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def helper(row):
            n = len(row)
            l, r = 0, n-1
            while l <= r:
                mid = (l+r)//2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1    
        
        for row in matrix:
            if helper(row):
                return True
            
        return False