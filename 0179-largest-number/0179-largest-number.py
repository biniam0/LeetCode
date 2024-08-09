from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def cmp(a, b):
            if a+b > b+a:
                return 1
            elif a == b:
                return 0
            else:
                return -1

        nums = [str(num) for num in nums]

        nums.sort(key=cmp_to_key(cmp), reverse=True)

        return "".join(nums).lstrip("0") or "0"