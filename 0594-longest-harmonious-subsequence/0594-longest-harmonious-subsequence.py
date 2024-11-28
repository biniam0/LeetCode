class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums_freq = Counter(nums)

        max_wind_size = 0
        for num in nums_freq.keys():
            if num+1 in nums_freq:
                max_wind_size = max(
                    max_wind_size, nums_freq[num] + nums_freq[num+1])

        return max_wind_size    