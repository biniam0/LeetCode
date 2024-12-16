class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # Optimized solution using MinHeap
        min_heap = []
        for i, num in enumerate(nums):
            heapq.heappush(min_heap, (num, i))

        while k > 0:
            min_num, idx = heapq.heappop(min_heap)
            pro = min_num * multiplier
            nums[idx] = pro
            heapq.heappush(min_heap, (pro, idx))
            k -= 1
        return nums

        # Bruteforce
        # while k > 0:
        #     min_num = min(nums)
        #     min_idx = nums.index(min_num)
        #     nums[min_idx] = min_num * multiplier
        #     k -= 1
        # return nums
