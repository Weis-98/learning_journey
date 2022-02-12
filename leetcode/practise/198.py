class Solution:
    def rob(self, nums: List[int]) -> int:
        mat = [[0 for i in range(len(nums)+1)], [0 for i in range(len(nums)+1)]]
        # 0行，此处不偷，1行，此处偷
        for i, ni in enumerate(nums):
            mat[0][i+1] = max(mat[1][i], mat[0][i])
            mat[1][i+1] = mat[0][i] + ni

        return max(mat[0][-1], mat[1][-1])

