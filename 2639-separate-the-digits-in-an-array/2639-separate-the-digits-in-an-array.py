class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            tmp = list(map(int, str(num)))
            res.extend(tmp)

        return res