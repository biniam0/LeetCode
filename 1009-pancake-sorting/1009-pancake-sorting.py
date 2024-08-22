class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        end = len(arr)
        res = []

        while end > 1:
            max_idx = arr.index(end)

            if max_idx == end - 1:
                end -= 1
                continue

            if max_idx != 0:
                arr[:max_idx + 1] = reversed(arr[:max_idx + 1])
                res.append(max_idx+1)

            arr[:end] = reversed(arr[:end])
            res.append(end)
            end -= 1

        return res