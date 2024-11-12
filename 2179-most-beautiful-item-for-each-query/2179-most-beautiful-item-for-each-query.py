class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        queries = sorted([(que, i) for i, que in enumerate(queries)])

        ans = [0] * len(queries)
        max_beauty, j = 0, 0
        for que, i in queries:
            while j < len(items) and items[j][0] <= que:
                max_beauty = max(max_beauty, items[j][1])
                j += 1
            ans[i] = max_beauty
        
        return ans
