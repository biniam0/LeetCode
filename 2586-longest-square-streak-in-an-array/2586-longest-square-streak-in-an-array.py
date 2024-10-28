class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        
        seen = {}
        for x in nums:
            if sqrt(x) in seen:
                seen[x] = seen[sqrt(x)]+1
            else:
                seen[x] = 1
        ans = max(seen.values())
        if ans >= 2:
            return ans
        return -1