class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_freq = Counter(nums)

        lower_bound = math.floor(len(nums)/3)
        res = []
        for num, freq in nums_freq.items():
            if freq > lower_bound:
                res.append(num)
        return res