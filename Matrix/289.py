class Solution(object):
    def gameOfLife(self, board):
        livingOnes = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1:
                    livingOnes.add((i,j))
                    
        def getNeighborCount(i,j):
            count = 0
            for x in range(max(0,i - 1),min(len(board),i + 2)):
                for y in range(max(0,j-1),min(len(board[0]),j+2)):
                    if (x != i or y != j) and (x,y) in livingOnes:
                        count += 1
            return count
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = getNeighborCount(i,j)
                if board[i][j] == 1:
                    if c < 2 or c > 3:
                        board[i][j] = 0
                else:
                    if c == 3:
                        board[i][j] = 1