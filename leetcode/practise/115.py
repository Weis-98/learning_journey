"""给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。

字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE"是"ABCDE"的一个子序列，而"AEC"不是）

题目数据保证答案符合 32 位带符号整数范围。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distinct-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""
class Solution:
    def numDistinct(self, s, t):
        len1 = len(s)
        len2 = len(t)
        if len1 < len2:
            return 0
        dp = [[0] * (len2 + 1) for i in range(len1 + 1)]
        for i in range(len1 + 1):
            dp[i][0] = 1
        for j in range(len2):
            for i in range(len1):
                if s[i] == t[j]:
                    dp[i + 1][j + 1] = dp[i][j] + dp[i][j + 1]
                else:
                    dp[i + 1][j + 1] = dp[i][j + 1]
        return dp[len1][len2]


s = Solution()
print(s.numDistinct(
    "babgbag",
    "bag"
))




