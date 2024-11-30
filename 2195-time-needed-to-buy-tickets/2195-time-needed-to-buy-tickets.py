class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total_time = 0

        ticket_idx = deque()

        for i, t in enumerate(tickets):
            ticket_idx.append((t, i))

        while ticket_idx:
            t, i = ticket_idx[0]
            if i == k and t == 1:
                total_time += 1
                break

            if t > 1:
                ticket_idx.popleft()
                ticket_idx.append((t-1, i))
                total_time += 1
            elif t == 1:
                ticket_idx.popleft()
                total_time += 1

        return total_time
