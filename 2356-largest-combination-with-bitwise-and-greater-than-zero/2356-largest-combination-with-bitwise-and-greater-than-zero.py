class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        count = [0] * 32
        for n in candidates:
            n_bit = bin(n)
            for i in range(-1, -len(n_bit), -1):
                if n_bit[i] == "1":
                    count[i] += 1
        return max(count)