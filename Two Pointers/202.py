class Solution(object):
    def isHappy(self, n):
        slow = self.squared(n)
        fast = self.squared(self.squared(n))

        while slow != fast and fast != 1:
            slow = self.squared(slow)
            fast = self.squared(self.squared(fast))
        
        return fast == 1

    def squared(self, n):
        res = 0
        while n > 0:
            temp = n % 10
            res += temp * temp
            n //= 10
        return res