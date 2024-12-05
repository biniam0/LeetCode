class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()

        con_floor = 0

        con_floor = max(con_floor, special[0] - bottom)

        l = 0
        for r in range(1, len(special)):
            if abs(special[r] - special[l]) > 1:
                con_floor = max(con_floor, abs(special[r]-special[l]-1))
            l += 1

        con_floor = max(con_floor, abs(special[-1] - top))

        return con_floor