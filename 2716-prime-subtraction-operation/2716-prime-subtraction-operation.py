class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def isPrime(n): 
            for f in range(2, int(sqrt(n))+1):
                if n % f == 0:
                    return False
            return True
        
        prev = 0
        for n in nums:
            upper_bound = n - prev # this upper bound is not inclusive

            largest_p = 0
            for i in range(upper_bound-1, 1, -1):
                if isPrime(i):
                    largest_p = i
                    break
            if n - largest_p <= prev:
                return False

            prev = n - largest_p

        return True


