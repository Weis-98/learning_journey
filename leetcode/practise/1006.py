class Solution:
    def clumsy(self, N: int) -> int:
        if N == 1:
            return 1
        if N == 2:
            return 2
        if N == 3:
            return 6
        if N == 4:
            return 7

        def f2(N: int):
            if N == 1:
                return -1
            if N == 2:
                return -2 * 1
            if N == 3:
                return int(-3 * 2 / 1)
            if N == 4:
                return int(-4 * 3 / 2) + 1
            if N > 4:
                return -int(N * (N - 1) / (N - 2)) + (N - 3) + f2(N - 4)

        if N > 4:
            return int(N*(N-1)/(N-2)+(N-3)) + f2(N-4)

        return f2(N)

s = Solution()
print(s.clumsy(7))