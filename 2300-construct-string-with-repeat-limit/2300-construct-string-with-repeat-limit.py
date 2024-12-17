class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # find the frequency of each character
        cnt_freq = Counter(s)
        ans = []

        # populate the heap with character ordinal value and the frequency
        max_heap = []
        for char, f in cnt_freq.items():
            char = -ord(char)
            heapq.heappush(max_heap, (char, f))

        while max_heap:
            char, f = heapq.heappop(max_heap)
            char = chr(-char)

            cur_f = min(repeatLimit, f)
            ans.append(char*cur_f)

            if f - cur_f > 0 and max_heap:
                nxt_char, nxt_f = heapq.heappop(max_heap)
                nxt_char = chr(-nxt_char)
                ans.append(nxt_char)

                if nxt_f > 1:
                    heapq.heappush(max_heap, (-ord(nxt_char), nxt_f-1))
                heapq.heappush(max_heap, (-ord(char), f-repeatLimit))

        return "".join(ans)
