class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique_arr = sorted(set(arr))

        rank_map = {num: i+1 for i, num in enumerate(unique_arr)}

        rank = [rank_map[num] for num in arr]

        return rank