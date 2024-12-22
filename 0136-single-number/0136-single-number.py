class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_freq = Counter()
        for num in nums:
            num_freq[num] += 1

        for num, f in num_freq.items():
            if f == 1:
                return num
