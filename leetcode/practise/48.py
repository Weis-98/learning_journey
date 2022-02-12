class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 1:
            return

        center = (n - 1) / 2
        for row in range(n // 2):
            for col in range((n + 1) // 2):
                hy = center - row
                hx = center - col
                matrix[row][col], matrix[int(center - hx)][int(center + hy)], matrix[int(center + hy)][
                    int(center + hx)], matrix[int(center + hx)][int(center - hy)] = matrix[int(center + hx)][
                                                                                        int(center - hy)], matrix[row][
                                                                                        col], matrix[int(center - hx)][
                                                                                        int(center + hy)], \
                                                                                    matrix[int(center + hy)][
                                                                                        int(center + hx)]
        return

