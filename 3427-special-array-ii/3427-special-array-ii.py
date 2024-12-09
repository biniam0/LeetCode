class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        prefix = [0]*n
        prefix[0] = 1
        res = []

        for i in range(1, n):
            if nums[i] & 1 == nums[i-1] & 1:
                prefix[i] = 1
            else:
                prefix[i] = 1+prefix[i-1]

        for i, q in enumerate(queries):
            l, r = q
            if prefix[r] >= (r-l+1):
                res.append(True)
            else:
                res.append(False)

        return res
