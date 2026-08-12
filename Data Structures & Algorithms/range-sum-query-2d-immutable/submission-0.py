class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        
        matrix.reverse()
        for row in matrix:
            row.reverse()

        pre = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                pre[i][j] = (
                    matrix[i-1][j-1]
                    + pre[i-1][j]
                    + pre[i][j-1]
                    - pre[i-1][j-1]
                )

        pre.pop(0)

        for row in pre:
            row.pop(0)
            row.reverse()

        pre.reverse()
        self.prev = pre

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = bottom = right = overlap = 0
        total = self.prev[row1][col1]
        if row2 < len(self.prev)-1:
            bottom = self.prev[row2+1][col1]
        if col2 < len(self.prev[0])-1:
            right = self.prev[row1][col2+1]

        if row2 < len(self.prev)-1 and col2 < len(self.prev[0])-1:
            overlap = self.prev[row2+1][col2+1]

        return total - (bottom+right) + overlap


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)