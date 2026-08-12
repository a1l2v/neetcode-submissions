class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = set()
        count = 0

        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    num = board[i][j]
                    if 0 <= int(num) <= 9:
                        res.add((i,num))
                        res.add((num,j))
                        res.add((i//3,j//3,num))
                        count += 3
        print(len(res))
        print(count)
        if len(res) == count:
            return True
        else:
            return False
        