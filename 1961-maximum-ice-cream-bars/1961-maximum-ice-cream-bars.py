class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        cnt = [0]*(max(costs)+1)
        for c in costs:
            cnt[c] += 1
        
        tot, bars = 0, 0
        for i in range(len(cnt)):
            if cnt[i] != 0:
                tmp = cnt[i]
                for j in range(1, tmp+1):
                    tot += i
                    if tot > coins:
                        break
                    elif tot == coins:
                        bars += 1
                        break
                    bars += 1

        return bars



