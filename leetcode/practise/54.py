# F1
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            matrix = list(zip(*matrix))[::-1]
        return res

# F2
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        width = len(matrix[0])
        height = len(matrix)
        L = 1 - 1
        R = width - 1
        U = 1 - 1
        D = height - 1
        while L <= R and U <= D:
            for i in range(L, R + 1):
                res.append(matrix[U][i])
            U += 1
            if L <= R and U <= D:
                pass
            else:
                break
            for i in range(U, D + 1):
                res.append(matrix[i][R])
            if L <= R and U <= D:
                pass
            else:
                break
            R -= 1
            for i in range(R, L - 1, -1):
                res.append(matrix[D][i])
            if L <= R and U <= D:
                pass
            else:
                break
            D -= 1
            for i in range(D, U - 1 , -1):
                res.append(matrix[i][L])
            L += 1
            if L <= R and U <= D:
                pass
            else:
                break
        return res