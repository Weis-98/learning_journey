class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        left = nums[0]
        ans = -1
        for num in nums:
            if num <= left:
                left = num
            else:
                ans = max(ans, num - left)
        return ans

