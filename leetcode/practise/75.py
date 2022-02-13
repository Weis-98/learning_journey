class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return

        left = 0
        right = n - 1

        i = 0
        while i <= right:
            while i <= right and nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
            i += 1
        return

