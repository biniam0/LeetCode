class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []

        list1_dict = defaultdict(list)
        list2_dict = defaultdict(list)

        for i, st in enumerate(list1):
            list1_dict[st].append(i)
        for i, st in enumerate(list2):
            list2_dict[st].append(i)

        tmp_dict = defaultdict(list)

        for word, idxs in list1_dict.items():
            if word in list2_dict:
                min_1 = min(idxs)
                min_2 = min(list2_dict[word])
                tmp_dict[word] = min_1 + min_2

        idx_sum = float("inf")
        for wrd, idx in tmp_dict.items():
            idx_sum = min(idx_sum, idx)

        for wrd in tmp_dict:
            if tmp_dict[wrd] == idx_sum:
                ans.append(wrd)
        return ans