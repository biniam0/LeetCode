class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        max_dig = "0"
        max_idx = -1
        swap_i, swap_j = -1, -1

        for i in reversed(range(len(num))):
            if num[i] > max_dig:
                max_dig = num[i]
                max_idx = i

            if num[i] < max_dig:
                swap_i = i
                swap_j = max_idx
        num[swap_i], num[swap_j] = num[swap_j], num[swap_i]
        return int("".join(num))