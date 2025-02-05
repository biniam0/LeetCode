class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = defaultdict(int)
        lose = defaultdict(int)

        for w, l in matches:
            win[w] += 1
            lose[l] += 1

        winners = []
        losers = []

        for k, v in win.items():
            if k not in lose:
                winners.append(k)

        for k, v in lose.items():
            if v == 1:
                losers.append(k)

        return [sorted(winners), sorted(losers)]