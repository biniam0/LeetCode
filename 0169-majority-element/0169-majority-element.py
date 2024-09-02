class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = Counter(nums)
        nums_dict = sorted(nums_dict.items(), key=lambda item: item[1])
        return nums_dict[-1][0]