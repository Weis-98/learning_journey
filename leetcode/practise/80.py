class Solution:
    def removeDuplicates(self, nums) -> int:
        n = len(nums)
        if n <= 2:
            return n
        while n - 2:
            if nums[n - 1] == nums[n - 3]:
                nums.pop(n - 3)
            n -= 1
        return len(nums)
