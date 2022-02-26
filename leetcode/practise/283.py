class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        快慢指针（双指针之一）
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] == 0:
                continue
            else:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return

