class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # Recursive Approach
        # MOD = 10**9 + 7

        # def countGood(n, i=0):
        #     if n == 0:
        #         return 1
        #     if i % 2 == 0:
        #         return 5 * countGood(n-1, i+1) % MOD
        #     else:
        #         return 4 * countGood(n-1, i+1) % MOD
        # return countGood(n)

        # Exponential Approach
        mod = 10**9 + 7
        even_pos = (n+1)//2
        prime_pos = n//2

        return (pow(5, even_pos, mod) * pow(4, prime_pos, mod))% mod
        # Iteration Approach
        # mod = 10**9 + 7
        # res = 1
        # for i in range(n):
        #     if i % 2 == 0:
        #         res = (res * 5) % mod
        #     else:
        #         res = (res * 4) % mod

        # return res