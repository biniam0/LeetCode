class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_cnt = Counter(s)
        t_cnt = Counter(t)
        if len(s) != len(t):
            return False
        for char in s_cnt:
            if char not in t_cnt:
                return False
            if s_cnt[char] != t_cnt[char]:
                return False
        return True


