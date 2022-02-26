class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        w = len(word)
        direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def check(i, j, k):
            # board[i][j] can or not satisfy word[k:]
            if board[i][j] != word[k]:
                return False

            if k == w - 1:
                return True

            visited.add((i, j))
            res = False
            for deltai, deltaj in direct:
                detecti = i + deltai
                detectj = j + deltaj
                if 0 <= detecti < m and 0 <= detectj < n and (detecti, detectj) not in visited:
                    if check(detecti, detectj, k + 1):
                        res = True
            visited.remove((i, j))
            return res

        for i in range(m):
            for j in range(n):
                if check(i, j, 0):
                    return True
        return False


