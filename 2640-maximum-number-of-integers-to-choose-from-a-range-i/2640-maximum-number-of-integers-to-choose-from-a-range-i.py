class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        cnt = 0
        cur_sum = 0

        for i in range(1, n+1):
            if i not in banned:
                if cur_sum + i <= maxSum:
                    cnt += 1
                    cur_sum += i
                else:
                    return cnt
        return cnt