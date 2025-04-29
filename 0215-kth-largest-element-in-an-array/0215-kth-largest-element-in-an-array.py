class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = heapq.heapify(nums)

        for _ in range(len(nums)-k):
            heapq.heappop(nums)
        
        return heappop(nums)