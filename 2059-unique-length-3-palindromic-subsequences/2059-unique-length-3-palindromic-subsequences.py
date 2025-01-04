class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = Counter(s)

        for m in s:
            right[m] -= 1
            for char in left:
                if right[char] > 0:
                    res.add((m, char))
            left.add(m)
        return len(res)