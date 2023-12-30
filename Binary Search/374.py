# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        s = 1
        while s <= n:
            m = (n + s) //2
            g = guess(m)
            if g == 0: return m
            if g == -1:
                n = m - 1
            if g == 1:
                s = m + 1

        
        