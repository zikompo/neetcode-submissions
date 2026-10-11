class Solution:
    def binary_search(self, l: int, r: int, lst: List[int], target: int):
        if l > r:
            return False
        m = l + (r-l) //2
        if lst[m] == target:
            return True
        elif lst[m] > target:
            return self.binary_search(l, m-1, lst, target)
        else:
            return self.binary_search(m+1, r, lst, target)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x, y = 0, len(matrix[0])-1
        for i, row in enumerate(matrix):
            if row[x] <= target <= row[y]:
                return self.binary_search(x, y, row, target)
        return False