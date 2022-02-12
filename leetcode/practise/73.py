class Solution:
    def  __init__(self):
        self.i = 0
        self.j = 1
    def __call__(self):
        

    def setZeroes(self, matrix):
        row, col = len(matrix), len(matrix[0])
        first_col = False
        for i in range(row):
            if matrix[i][0] == 0:
                first_col = True
            for j in range(1, col):  # 把第一个位置让出来 给后面的[0][0]判断留空间
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(col):
                matrix[0][j] = 0

        if first_col:
            for j in range(row):
                matrix[j][0] = 0