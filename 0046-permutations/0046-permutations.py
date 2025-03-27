class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perm = self.permute(nums)
            
            for p in perm:
                p.append(n)
            ans.extend(perm)
            nums.append(n)
        return ans
        if len(nums) == 0:
            return [[]]

        perm = self.permute(nums[1:])
        res = []
        for p in perm:
            for i in range(len(p)+1):
                pc = p.copy()
                pc.insert(i, nums[0])
                res.append(pc)
        return res
