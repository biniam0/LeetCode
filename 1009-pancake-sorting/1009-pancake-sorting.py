class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        rnd, n, ans = 0, len(arr), []
        while rnd < n:
            max_idx = arr.index(max(arr[:n-rnd]))
            if max_idx != n-rnd-1:
                if max_idx != 0:
                    ans.append(max_idx+1)
                    l, r = 0, max_idx
                    while l < r:
                        arr[l], arr[r] = arr[r], arr[l]
                        l += 1
                        r -= 1
                ans.append(n-rnd)
                i, j = 0, n-rnd-1
                while i < j and j < n:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
            rnd += 1
        return ans