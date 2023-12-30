class Solution(object):
    def minCostClimbingStairs(self, cost):
        if not cost: return 0

        dp0, cur = cost[0], 0
        dp1 = cost[1] if len(cost) >= 2 else cost[0]

        for i in range(2, len(cost)):
            cur = cost[i] + min(dp0, dp1)
            dp0, dp1 = dp1, cur
        return min(dp0, dp1)