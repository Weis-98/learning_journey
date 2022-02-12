class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            A = {
                0: 1,
                1: 1
            }
            flag = 2
            while flag <= n:
                temp = 0
                for i in range(flag):
                    temp = temp + A[i] * A[flag - 1 - i]
                A[flag] = temp
                flag += 1

        return A[n]