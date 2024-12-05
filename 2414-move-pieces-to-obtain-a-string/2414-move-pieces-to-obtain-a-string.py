class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)

        f = s = 0
        last_idx = -1

        while f < n and s < n:
            while f < n and start[f] == "_":
                f += 1
            while s < n and target[s] == "_":
                s += 1


            if f == n and s == n:
                return True

            if f < n and s < n and start[f] != target[s]:
                return False
            if f < n and s < n and start[f] == "L" and (s <= last_idx or s > f):
                return False
            elif f < n and s < n and start[f] == "R" and f > s:
                return False
            if last_idx <= f <= s:
                last_idx = s

            s += 1
            f += 1
        while f < n and start[f] == "_":
            f += 1
        while s < n and target[s] == "_":
            s += 1

        return f == n and s == n
