class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = defaultdict(int)
        for num in arr:
            freq[((num % k)+k) % k] += 1
            
        if freq[0] % 2 != 0:
            return False

        for i in range(1, k):
            if freq[i] != freq[k-i]:
                return False
        return True