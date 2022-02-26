class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = [-1] * n
        for i in range(n):
            temp = i
            flag = 1
            for row in range(m):
                if grid[row][temp] == 1 and temp + 1 < n and grid[row][temp + 1] == 1:
                    temp += 1
                elif grid[row][temp] == -1 and temp - 1 > -1 and grid[row][temp - 1] == -1:
                    temp -= 1
                else:
                    flag = 0
                    break
            if flag:
                ans[i] = temp
            else:
                ans[i] = -1
        return ans

