class Solution(object):
    def numTilings(self, n):
        dp = [1,2,5] + [0] * n
        for i in range(3, n):
            dp[i] = (2 * dp[i-1] + dp[i-3]) % (10**9+7)
        return dp[n - 1]
