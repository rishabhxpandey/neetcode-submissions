class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        start, end = 0, len(matrix) * len(matrix[0])-1

        while start <= end:

            mid = (start + end) // 2
            r, c = divmod(mid, cols)
            mid_elem = matrix[r][c]

            if mid_elem == target:
                return True
            elif mid_elem > target:
                end = mid - 1
            else:
                start = mid + 1
        return False