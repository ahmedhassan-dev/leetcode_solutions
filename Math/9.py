class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        temp = x
        reserved = 0
        while temp != 0:
            reserved = reserved*10 + temp %10
            temp //=10 
        return x == reserved
