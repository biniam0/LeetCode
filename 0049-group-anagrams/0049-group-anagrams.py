class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = defaultdict(list)

        for char in strs:
            tmp = "".join(sorted(char))
            strs_dict[tmp] += [char]
        res = [lists for lists in strs_dict.values()]
        return res

