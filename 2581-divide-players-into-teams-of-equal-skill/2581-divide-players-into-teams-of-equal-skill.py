class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        if sum(skill) % (n//2) != 0:
            return -1

        skill_weight = sum(skill)/(n//2)
        skill.sort()
        l, r = 0, len(skill)-1
        t_skill: int = 0

        while l < r:
            if skill_weight != (skill[l] + skill[r]):
                return -1
            t_skill += (skill[l] * skill[r])
            l += 1
            r -= 1
        return t_skill
