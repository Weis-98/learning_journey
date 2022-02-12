class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        begin = 0
        max_len = 0

        dp = [[False] * len(s) for _ in range(n)]

        for i in range(n):
            dp[i][i] == True

        for L in range(1, n + 1):
            for i in range(n):
                j = i + L - 1
                if j >= n:
                    break
                dp[i][j] = (s[i] == s[j]) and (i + 1 >= j - 1 or dp[i + 1][j - 1])
                if dp[i][j] and j - i + 1 > max_len:
                    begin = i
                    max_len = j - i + 1

        return s[begin: begin + max_len]

