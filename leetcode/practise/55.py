class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        F1 动态规划
        :param nums:
        :return:
        """
        n = len(nums)
        if n == 1:
            return True
        if nums[0] == 0:
            return False

        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] - 1, nums[i])
            if dp[i] == 0 and i < n - 1:
                return False

        return True

    def canJump(self, nums: List[int]) -> bool:
        """
        F2 省空间的动态规划
        :param nums:
        :return:
        """
        n = len(nums)
        if n == 1:
            return True
        if nums[0] == 0:
            return False

        pre = nums[0]
        for i in range(1, n):
            pre = max(pre - 1, nums[i])
            if pre == 0 and i < n - 1:
                return False

        return True
    def canJump(self, nums: List[int]) -> bool:
        """
        F3
        :param nums:
        :return:
        """
        n = len(nums)
        right = 0
        for i in range(n):
            if i <= right:
                right = max(nums[i] + i, right)
                if right >= n - 1:
                    return True
            else:
                break
        return False



