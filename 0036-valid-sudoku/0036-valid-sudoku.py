class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])

        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] != ".": 
                    if board[j][i] in seen:
                        return False
                    seen.add(board[j][i])

        def helper(start_row, start_col):
            seen = set()
            for l in range(3):
                for r in range(3):
                    current_value = board[start_row + l][start_col + r]
                    if current_value != '.':
                        if current_value in seen:
                            return False
                        seen.add(current_value)

            return True

        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                if not helper(start_row, start_col):
                    return False
        return True