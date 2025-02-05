class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_freq = Counter(chars)
        ans = 0

        for word in words:
            tmp_cnt = Counter(word)
            for c, f in tmp_cnt.items():
                if f > char_freq[c]:
                    break
            else:
                ans += len(word)

        return ans
