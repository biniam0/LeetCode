class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])

        max_values = [0] * len(events)
        max_so_far = 0
        res = 0

        def find_last_non_overlapping(index):
            low, high = 0, index - 1
            while low <= high:
                mid = (low + high) // 2
                if events[mid][1] < events[index][0]:
                    if events[mid + 1][1] < events[index][0]:
                        low = mid + 1
                    else:
                        return mid
                else:
                    high = mid - 1
            return -1

        for i in range(len(events)):
            start, end, value = events[i]

            max_so_far = max(max_so_far, value)

            last_index = find_last_non_overlapping(i)
            if last_index != -1:

                res = max(res, value + max_values[last_index])
            else:

                res = max(res, value)

            max_values[i] = max_so_far

        return res