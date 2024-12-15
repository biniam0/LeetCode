class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_heap = []

        def helper(p, t):
            cur_avg = p/t
            new = (p+1)/(t+1)
            return new - cur_avg

        for i, (p, t) in enumerate(classes):
            incr = helper(p, t)
            heapq.heappush(max_heap, (-incr, i))

        while extraStudents > 0:
            _, idx = heapq.heappop(max_heap)
            classes[idx][0] += 1
            classes[idx][1] += 1
            incr = helper(classes[idx][0], classes[idx][1])
            heapq.heappush(max_heap, (-incr, idx))
            extraStudents -= 1
        sum_ = 0
        for p, t in classes:
            sum_ += (p/t)
        # sum_ = sum(p/t for p, t in classes)
        return sum_/len(classes)