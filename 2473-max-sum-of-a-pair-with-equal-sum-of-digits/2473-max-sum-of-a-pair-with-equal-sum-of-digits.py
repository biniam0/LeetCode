class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sumDigits(n):
            tot = 0
            while n:
                tot += n % 10
                n //= 10
            return tot
        digit_sums = defaultdict(list)
        for num in nums:
            d_num = sumDigits(num)
            digit_sums[d_num].append(num)
        flag = False
        for numbers in digit_sums.values():
            if len(numbers) >= 2:
                flag = True 
        if not flag:
            return -1
        max_sum = float("-inf")
        for ds, numbers in digit_sums.items():
            if len(numbers) < 2:
                continue
            numbers.sort(reverse=True)
            max_sum = max(numbers[0] + numbers[1], max_sum)
        return max_sum