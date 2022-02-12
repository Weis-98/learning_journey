class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        dp[0][0] = True

        for i in range(1 + len(s)):
            for j in range(1, 1 + len(p)):

                if p[j - 1] == '*':
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i - 1][j]
                    dp[i][j] = dp[i][j] or dp[i][j - 2]
                else:
                    if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]

        return dp[len(s)][len(p)]

