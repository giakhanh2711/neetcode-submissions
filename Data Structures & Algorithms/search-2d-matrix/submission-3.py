class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrow, ncol = len(matrix), len(matrix[0])
        left, right = 0, nrow * ncol - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            r, c = mid // ncol, mid % ncol
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False