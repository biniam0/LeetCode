class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1*num for num in nums]
        maxheap = nums
        heapq.heapify(maxheap)

        ans = 0
        for i in range(k):
            ans = heapq.heappop(maxheap)

        return -ans
