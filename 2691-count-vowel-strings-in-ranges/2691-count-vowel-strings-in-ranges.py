class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(("a", "e", "i", "o", "u"))
        res = []

        prefix_cnt = [0] * (len(words)+1)
        prev = 0
        for i, w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                prev += 1
            prefix_cnt[i+1] = prev

        for l, r in queries:
            res.append(prefix_cnt[r+1] - prefix_cnt[l])

        return res