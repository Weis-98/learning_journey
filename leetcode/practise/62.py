class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 组合数(m + n - 2, m - 1)
        m, n = max(m, n), min(m, n)
        ans = 1
        for i in range(1, n):
            ans = ans * (m - 1 + i) // i
        return ans


s = Solution()
print(s.uniquePaths(3, 2))