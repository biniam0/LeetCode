class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums_freq = Counter(nums)

        ans = []

        for num, freq in nums_freq.items():
            if freq == 2:
                ans.append(num)
        return ans