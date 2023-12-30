class Solution(object):
    def setZeroes(self, matrix):
        col0, rows, cols = 1, len(matrix), len(matrix[0])

        for i in xrange(0, rows):
            if matrix[i][0] == 0:
                col0 = 0
            for j in xrange(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in xrange(rows-1, -1, -1):
            for j in xrange(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0


        