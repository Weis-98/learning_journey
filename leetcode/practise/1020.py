class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visit = [[False] * col for _ in range(row)]

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or visit[r][c] or grid[r][c] == 0:
                return
            visit[r][c] = True
            for R, C in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                dfs(R, C)

        for r in range(row):
            dfs(r, 0)
            dfs(r, col - 1)
        for c in range(col):
            dfs(0, c)
            dfs(row - 1, c)

        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and visit[i][j] == False:
                    res += 1
        return res

