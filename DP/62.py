class Solution(object):
    def uniquePaths(self, m, n):
        cur_row = prev_row = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur_row[j] = cur_row[j-1] + prev_row[j]
            cur_row, prev_row = prev_row, cur_row
        return prev_row[-1]
