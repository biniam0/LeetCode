class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        score = 0
        min_heap = [(val, idx) for idx, val in enumerate(nums)]
        heapq.heapify(min_heap)
        seen = set()

        while min_heap:
            val, idx = heapq.heappop(min_heap)
            if idx in seen:
                continue
            score += val
            seen.add(idx)

            if idx-1 >= 0:
                seen.add(idx-1)
            if idx+1 < n:
                seen.add(idx+1)

        return score