class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []

        for i in range(n):
            temp = nums[i:i+k]
            is_power = True
            for j in range(1, len(temp)):
                if temp[j-1]+1 != temp[j]:
                    is_power = False

            if is_power:
                res.append(max(temp))
            else:
                res.append(-1)
            if i+k == n:
                break
        return res