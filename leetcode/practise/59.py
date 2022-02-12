class Solution:
    def generateMatrix(self, n):
        matrix = []
        num = 1
        for i in range(n):
            matrix.append([0 for i in range(n)])
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            for j in range(top + 1, bottom + 1):
                matrix[j][right] = num
                num += 1
            if top < bottom and left < right:
                for i in range(right - 1, left - 1, -1):
                    matrix[bottom][i] = num
                    num += 1
                for j in range(bottom - 1, top, -1):
                    matrix[j][left] = num
                    num += 1
            top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1
        return matrix