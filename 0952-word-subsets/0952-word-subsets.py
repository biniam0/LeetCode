class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = []

        base_map = defaultdict(int)

        for w2 in words2:
            w2_map = Counter(w2)
            for val_2, freq_2 in w2_map.items():
                base_map[val_2] = max(base_map[val_2], freq_2)

        for w1 in words1:
            w1_map = Counter(w1)

            for b_val, b_freq in base_map.items():
                if w1_map[b_val] < b_freq:
                    break
            else:
                ans.append(w1)

        return ans