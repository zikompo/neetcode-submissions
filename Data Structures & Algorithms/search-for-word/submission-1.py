class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(board), len(board[0])

        def isValid(r, c):
            return 0<=r<rows and 0<=c<cols

        def bt(r, c, k, visited):
            if board[r][c] != word[k]:
                return False
            if k == len(word)-1:
                return True
        
            for dr, dc in directions:
                if isValid(r+dr, c+dc) and (r+dr, c+dc) not in visited:
                    visited.add((r+dr, c+dc))
                    found = bt(r+dr, c+dc, k+1, visited)
                    visited.remove((r+dr, c+dc))
                    if found:
                        return True

            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and bt(r, c, 0, {(r, c)}):
                    return True
            
        return False

