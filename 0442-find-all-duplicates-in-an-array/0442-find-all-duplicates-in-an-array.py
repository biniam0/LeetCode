class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        ans = []

        for num in nums:
            if num in seen:
                ans.append(num)
                continue
            seen.add(num)

        return ans