class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0]*len(nums)
        prod = 1
        flag = False
        for n in nums:
            if n == 0:
                flag = True
                continue
            else:
                prod *= n
        ans = []
        for n in nums:
            if n == 0:
                ans.append(prod)
                continue
            if flag:
                ans.append(0)
            else:
                ans.append(prod//n)
        return ans