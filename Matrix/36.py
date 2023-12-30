class Solution(object):
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x != '.':
                    res += [(i,x), (x,j), (i // 3,j // 3,x)]
        return len(res) == len(set(res))
        