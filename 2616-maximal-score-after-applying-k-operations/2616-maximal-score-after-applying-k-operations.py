class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0

        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)

        while k:
            n = abs(heapq.heappop(max_heap))
            score += n
            n = -math.ceil(n/3)
            heapq.heappush(max_heap, n)
            k -= 1

        return score
