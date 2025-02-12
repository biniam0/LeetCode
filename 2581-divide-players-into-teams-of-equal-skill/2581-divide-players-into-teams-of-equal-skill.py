class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l, r = 0, len(skill)-1
        base = skill[l] + skill[r]
        ans = 0
        while l < r:
            sum_ = skill[l] + skill[r]
            if base != sum_:
                return -1

            ans += (skill[l]*skill[r])
            l += 1
            r -= 1
        return ans