class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = defaultdict(int)

        for row in matrix:
            row_key = tuple(row)

            if not row[0]:
                row_key = tuple([0 if bit else 1 for bit in row])
            count[row_key] += 1

        return max(count.values())
