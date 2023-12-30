class Solution(object):
    def maxProfit(self, prices, fee):
        profit, pre_min = 0, prices[0]
        for p in prices:
            if p > pre_min + fee:
                profit += p - pre_min - fee
                pre_min = p - fee
            else:
                pre_min = min(pre_min, p)
        return profit
        