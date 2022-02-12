class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        res = 10 ** 5
        for i in range(0, len(nums) - k + 1):
            if nums[i + k - 1] - nums[i] < res:
                res = nums[i + k - 1] - nums[i]

        return res

