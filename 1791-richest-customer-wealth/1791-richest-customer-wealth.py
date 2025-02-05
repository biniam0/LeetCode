class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0

        for cust in accounts:
            ans = max(ans, sum(cust))

        return ans