class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Using Heap + Custom Comparator        
        class LargerStrComparator(str):
            def __lt__(self, other):
                return self + other > other + self 

        if not any(nums):
            return  "0"

        heap = []
        for num in nums:
            heapq.heappush(heap, LargerStrComparator(str(num)))
            
        ans = ""
        while heap:
            ans += heapq.heappop(heap)
        return ans

        # nums_str = list(map(str, nums))
        # nums_str.sort(key=lambda a: 10*a, reverse=True)
        # if nums_str[0] == "0":
        #     return "0"
        # return "".join(nums_str)


