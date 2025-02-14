class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0 
        ans = float("-inf")
        hash = defaultdict(int)
        for r in range(len(fruits)):
            hash[fruits[r]]+= 1
            while l < len(fruits) and len(hash) > 2:
                hash[fruits[l]] -= 1
                if hash[fruits[l]] == 0:
                    del hash[fruits[l]]
                l += 1
            ans = max(ans, sum(hash.values()))

        return ans
