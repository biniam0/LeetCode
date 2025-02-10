class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []

        count = Counter(arr1)

        for i in range(len(arr2)):
            tmp = [arr2[i]] * count[arr2[i]]
            del count[arr2[i]]
            ans.extend(tmp)
        count = dict(sorted(count.items(), key=lambda item: item[0]))
        for val, freq in count.items():
            ans.extend([val]*freq)
        return ans