class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m, n = len(grid), len(grid[0])

        sequence = []
        counts = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    counts += 1
                    sequence.append((i, j))
                    grid[i][j] = "0"
                    while sequence:
                        temp = sequence[0]
                        sequence.remove(temp)
                        if temp[0] - 1 >= 0 and grid[temp[0] - 1][temp[1]] == "1":
                            sequence.append((temp[0] - 1, temp[1]))
                            grid[temp[0] - 1][temp[1]] = "0"
                        if temp[1] - 1 >= 0 and grid[temp[0]][temp[1] - 1] == "1":
                            sequence.append((temp[0], temp[1] - 1))
                            grid[temp[0]][temp[1] - 1] = "0"
                        if temp[0] + 1 < m and grid[temp[0] + 1][temp[1]] == "1":
                            sequence.append((temp[0] + 1, temp[1]))
                            grid[temp[0] + 1][temp[1]] = "0"
                        if temp[1] + 1 < n and grid[temp[0]][temp[1] + 1] == "1":
                            sequence.append((temp[0], temp[1] + 1))
                            grid[temp[0]][temp[1] + 1] = "0"

        return counts

