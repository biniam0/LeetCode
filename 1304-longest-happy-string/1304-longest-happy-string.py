class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res, max_heap = "", []

        for cnt, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if cnt != 0:
                heapq.heappush(max_heap, (cnt, char))

        while max_heap:
            cnt, char = heapq.heappop(max_heap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not max_heap:
                    break
                cnt2, char2 = heapq.heappop(max_heap)
                res += char2
                cnt2 += 1
                if cnt2:
                    heapq.heappush(max_heap, (cnt2, char2))
            else:
                res += char
                cnt +=1
            if cnt:
                heapq.heappush(max_heap, (cnt, char))
                
        return res




    

