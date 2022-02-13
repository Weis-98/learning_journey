class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        F1
        :param nums:
        :return:
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        maxsum = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            if dp[i] > maxsum:
                maxsum = dp[i]

        return maxsum

    def maxSubArray(self, nums: List[int]) -> int:
        """
        F2
        :param nums:
        :return:
        """
        pre = nums[0]
        maxsum = pre
        for i in range(1, len(nums)):
            pre = max(pre + nums[i], nums[i])
            if pre > maxsum:
                maxsum = pre
        return pre




