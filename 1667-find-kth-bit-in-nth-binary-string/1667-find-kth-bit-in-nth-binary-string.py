class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # The Recursion Solution
        length = 2**n -1
        
        def helper(length, k):
            if length == 1:
                return "0"

            half = length // 2
            if k <= half:
                return helper(half, k)
            elif k> half+1:
                res = helper(half, 1 + length -k)
                return "0" if res == "1" else "1"
            else:
                return "1"
        return helper(length, k)

        # Not Efficient 
        # def buildTheBit(n):
        #     s_1 = "0"
        #     for i in range(n):
        #         list_s = list(s_1)

        #         # For inverting the string
        #         for i in range(len(list_s)):
        #             if list_s[i] == "1":
        #                 list_s[i] = "0"
        #             else:
        #                 list_s[i] = "1"

        #         s_1 = s_1 + "1" + "".join(reversed(list_s))

        #     return s_1

        # s_n = buildTheBit(n)

        # return s_n[k-1]
        
        # Iterative Solution
        # length = 2**n -1
        # invert = False
        # while length > 1:
        #     half = length // 2

        #     if k <= half:
        #         length = half
        #     elif k > half + 1:
        #         K = 1 + length - k
        #         length = half
        #         invert = not invert
        #     else:
        #         return "1" if not invert else "0"
        # return "0" if not invert else "1"