class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        F1 DP
        :param prices:
        :return:
        '''
        ans = 0
        n = len(prices)
        dp = [[0] * 2] * n
        dp[0][1] = - prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i][0] - prices[i])

        return dp[n - 1][0]

    def maxProfit(self, prices: List[int]) -> int:
        """
        F2
        :param prices:
        :return:
        """
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                ans += prices[i] - prices[i - 1]
        return ans

