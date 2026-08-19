class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = (m*n) - 1

        while(left<=right):
            mid = (left+right)//2

            ele = matrix[mid//n][mid%n]

            if ele > target:
                right = mid - 1
            elif ele < target:
                left = mid+1 
            else:
                return True

        return False
