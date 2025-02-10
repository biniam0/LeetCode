class Solution:
    def frequencySort(self, s: str) -> str:
        char_freq = Counter(s)
        char_freq = dict(sorted(char_freq.items(), key = lambda item: item[1], reverse=True))

        ans = ""

        for char, freq in char_freq.items():
            ans += char*freq

        return ans