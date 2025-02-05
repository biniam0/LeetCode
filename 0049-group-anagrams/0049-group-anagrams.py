class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ = defaultdict(list)

        for w in strs:
            tmp = "".join(sorted((w)))
            dict_[tmp].append(w)

        return list(dict_.values())
            