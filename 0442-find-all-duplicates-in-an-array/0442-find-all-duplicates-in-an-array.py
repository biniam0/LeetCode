class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            num = abs(num)
            if nums[num-1] < 0:
                ans.append(num)
            nums[num-1] *= -1
        return ans

        
        
        # seen = set()
        # ans = []

        # for num in nums:
        #     if num in seen:
        #         ans.append(num)
        #         continue
        #     seen.add(num)

        # return ans