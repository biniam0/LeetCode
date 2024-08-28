class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        even_pos = (n+1)//2
        prime_pos = n//2

        return (pow(5, even_pos, mod) * pow(4, prime_pos, mod))% mod
        
        # mod = 10**9 + 7
        # res = 1
        # for i in range(n):
        #     if i % 2 == 0:
        #         res = (res * 5) % mod
        #     else:
        #         res = (res * 4) % mod

        # return res