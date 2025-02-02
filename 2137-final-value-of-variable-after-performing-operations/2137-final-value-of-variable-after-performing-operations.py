class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        plus_cnt = minus_cnt = 0

        for ops in operations:
            if ops == "++X" or ops == "X++":
                plus_cnt += 1
            else:
                minus_cnt += 1

        return plus_cnt - minus_cnt    