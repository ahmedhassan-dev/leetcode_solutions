class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        maxProfit = 0
        for p in prices:
            if p < buy:
                buy = p
            elif maxProfit < p - buy:
                maxProfit = p - buy
        return maxProfit

            

        