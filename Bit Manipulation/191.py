class Solution(object):
    def hammingWeight(self, n):
        res = 0
        while n != 0:
            if n & 1 == 1:
                res += 1
            n >>= 1
        return res
        