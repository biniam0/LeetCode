class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_freq = Counter(text)
        base_size = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}

        min_num = float("+inf")
        for char, freq in base_size.items():
            min_num = min(min_num, (text_freq[char] // base_size[char]))

        return min_num
