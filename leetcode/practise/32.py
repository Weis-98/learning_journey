class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        F1 动态规划
        :param s:
        :return:
        """
        dp = [0] * len(s)
        max_couple = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    if i - 2 >= 0:
                        dp[i] = 2 + dp[i - 2]
                    else:
                        dp[i] = 2
                else:
                    if i - dp[i - 1] >= 1 and s[i - dp[i - 1] - 1] == '(':
                        if i - dp[i - 1] >= 2:
                            dp[i] = dp[i - dp[i - 1] - 2] + dp[i - 1] + 2
                        else:
                            dp[i] = dp[i - 1] + 2
        for i in dp:
            if i > max_couple:
                max_couple = i

        return max_couple

    def longestValidParentheses(self, s: str) -> int:
        """
        F2 堆栈
        :param s:
        :return:
        """
