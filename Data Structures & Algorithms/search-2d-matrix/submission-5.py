class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if (len(matrix) == len(matrix[0])==1) and matrix[0][0] != target:
            return False
        
        m = 0
        n = len(matrix[0])-1
        if matrix[m][n] == target:
            return True
        elif matrix[m][n] < target:
            if m+1 > len(matrix)-1:
                return False
            return self.searchMatrix(matrix[m+1:][:], target)
        else:
            if n-1 < 0:
                return False
            return self.searchMatrix([sub[:n] for sub in matrix], target)

