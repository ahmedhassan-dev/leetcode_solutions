class Solution(object):
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]
        pascal = [[1], [1, 1]]
        for i in range(2, numRows):
            new_row = [1] + [pascal[-1][j-1] + pascal[-1][j] for j in range(1,i)] + [1] 
            pascal.append(new_row)
        return pascal

