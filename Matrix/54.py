class Solution(object):
    def spiralOrder(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix)[::-1])
        return res