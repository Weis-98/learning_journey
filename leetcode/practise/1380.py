class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        rowmin = [0] * m
        colmax = [0] * n
        ans = []

        for j in range(n):
            colmax[j] = max([matrix[i][j] for i in range(m)])

        for i in range(m):
            rowmin[i] = min(matrix[i])
            for j in range(n):
                if matrix[i][j] == rowmin[i] and matrix[i][j] == colmax[j]:
                    ans.append(matrix[i][j])
        return ans

