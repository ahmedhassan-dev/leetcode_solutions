class Solution(object):
    def tribonacci(self, n):
        if n < 2: return n
        if n == 2: return 1
        a,b,c,d = 0,1,1,0
        for _ in range(3, n+1):
            d=a+b+c
            a,b,c=b,c,d
        return c
        