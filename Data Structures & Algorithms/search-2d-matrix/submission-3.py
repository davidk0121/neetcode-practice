class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen, colLen = len(matrix), len(matrix[0])
        top, bot = 0, rowLen - 1
        mid = 0
        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                break
        
        l, r = 0, colLen - 1
        m = 0
        while l <= r:
            m = (l + r) // 2
            if matrix[mid][m] < target:
                l = m + 1
            elif matrix[mid][m] > target:
                r = m - 1
            else:
                return True
        return matrix[mid][m] == target