class Solution:
    def maximumLength(self, s: str) -> int:
        top_3_freq = [[-1, -1, -1] for _ in range(26)]

        wind_size = 0
        last_seen = ""

        for char in s:
            idx = ord(char) - ord("a")
            wind_size = wind_size + 1 if char == last_seen else 1
            last_seen = char
            min_idx = top_3_freq[idx].index(min(top_3_freq[idx]))

            if wind_size > top_3_freq[idx][min_idx]:
                top_3_freq[idx][min_idx] = wind_size

        max_len = -1
        for freq in top_3_freq:
            max_len = max(max_len, min(freq))

        return max_len
        # s_freq = defaultdict(int)
        # ans = -1

        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         s_freq[s[i:j+1]] += 1

        # for s, f in s_freq.items():
        #     if len(set(s)) == 1 and f >= 3:
        #         ans = max(ans, len(s))

        # return ans