class RecentCounter:

    def __init__(self):
        self.cnt = 0
        self.queue = deque()
        

    def ping(self, t: int) -> int:
        self.queue.append(t)
        rg = [t-3000, t]
        ans = 0

        while self.queue[0] < rg[0]:
            self.queue.popleft()

        return len(self.queue)

        # for time in self.queue:
        #     if rg[0] <= time <= rg[1]:
        #         ans += 1
        # return ans
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)