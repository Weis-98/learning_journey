class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        特别需要注意的一点：
        不能够使用[[0] * 9] * 9！
        对于一个list的乘法是仅仅拷贝了指针，而不是深拷贝，也就是说内部其实是同一个list
        :param board:
        :return:
        """
        row = [[0] * 9 for _ in range(9)]
        col = [[0] * 9 for _ in range(9)]
        sub = [ [ [0] * 9 for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    index = int(board[i][j]) - 1
                    row[i][index] += 1
                    col[j][index] += 1
                    sub[i // 3][j // 3][index] += 1
                    if row[i][index] > 1 or col[j][index] > 1 or sub[i // 3][j // 3][index] > 1:
                        return False
        return True

