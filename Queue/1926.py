class Solution(object):
    def nearestExit(self, maze, entrance):
        rows, cols = len(maze), len(maze[0])
        maze[entrance[0]][entrance[1]] = '+'
        q = collections.deque()
        q.append([entrance[0], entrance[1], 0])
        while q:
            x, y, steps = q.popleft()
            for r, c in [[x+1, y],[x-1, y], [x,y+1], [x,y-1]]:
                if 0 <= r < rows and 0<= c < cols and maze[r][c] == '.':
                    if r == 0 or r == cols-1 or c == 0 or c == cols-1:
                        return steps+1
                    maze[r][c] = '+'
                    q.append([r,c,steps+1])
        return -1