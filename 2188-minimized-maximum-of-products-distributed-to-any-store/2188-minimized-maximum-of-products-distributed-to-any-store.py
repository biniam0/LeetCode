class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def helper(i):
            total_store = 0
            for char in quantities:
                total_store += ceil(char/i)
            return total_store <= n
        
        l, r = 1, max(quantities)
        ans = 0
        while l <= r:
            mid = (l+r)//2
            if helper(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

