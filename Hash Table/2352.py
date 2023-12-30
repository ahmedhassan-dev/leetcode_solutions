class Solution(object):
    def equalPairs(self, grid):
        tpse = Counter(zip(*grid))
        grid = Counter(map(tuple,grid))
        return sum(grid[t]*tpse[t] for t in tpse)