# Time complexity: O(rows * cols) -> each cell is visited at least once
# Space complexity: O(rows * cols) -> in the worst case if all the oranges are rotten they will be added to the queue

class Solution(object):
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        if rows == 0: return -1
        fresh_cnt, rotten = 0, deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh_cnt += 1

        minutes_passed = 0
        while rotten and fresh_cnt > 0:
            minutes_passed += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for xd, yd in [(1,0), (-1,0), (0,1), (0,-1)]:
                    xx, yy = x + xd, y + yd
                    if xx < 0 or yy < 0 or xx == rows or yy == cols:
                        continue
                    if grid[xx][yy] == 2 or grid[xx][yy] == 0:
                        continue

                    fresh_cnt -= 1
                    grid[xx][yy] = 2
                    rotten.append((xx,yy))
        return minutes_passed if fresh_cnt == 0 else -1