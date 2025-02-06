class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:


        if len(nums) < 4:
            return 0

        p_freq = Counter()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                p_freq[nums[i] * nums[j]] += 1

        ans = 0

        for prod, freq in p_freq.items():
            ans +=  (freq * (freq-1) * 4)

        return ans 

        
