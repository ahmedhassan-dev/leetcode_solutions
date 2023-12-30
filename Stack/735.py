class Solution(object):
    def asteroidCollision(self, asteroids):
        # O(n) time comp
        res = []
        for ast in asteroids:
            while len(res) and ast < 0 and res[-1] > 0:
                if res[-1] == -ast:
                    res.pop()
                    break
                elif res[-1] < -ast:
                    res.pop()
                    continue
                else:
                    break
            else:
                res.append(ast)
        return res  