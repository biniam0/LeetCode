class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0

        for num, f in count.items():
            if f > 1:
                ans += (f*(f-1))//2

        return ans