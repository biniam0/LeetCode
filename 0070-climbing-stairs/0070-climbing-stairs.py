class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        stack = [1, 2]
        i = 0
        while i < n-2:
            stack.append(stack[-1] + stack[-2])
            i += 1
        return stack[-1]


































        # if n <= 2:
        #     return n
        # prev2 = 1
        # prev1 = 2

        # for i in range(3, n+1):
        #     current = prev1 + prev2
        #     prev2 = prev1
        #     prev1 = current

        # return prev1