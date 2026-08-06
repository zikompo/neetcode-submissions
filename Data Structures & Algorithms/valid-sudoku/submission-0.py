class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            rows = {}
            for entry in row:
                if entry in rows and entry != '.':
                    print("No")
                    return False
                rows[entry] = 1
        for col in range(9):
            cols = {}
            for row in board:
                if row[col] in cols and row[col] != '.':
                    return False
                cols[row[col]] = 1
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                squares = {}
                for row in range(3):
                    for col in range(3):
                        if board[row+i][col+j] in squares and board[row+i][col+j] != '.':
                            return False
                        squares[board[row+i][col+j]] = 1
        return True
            
            