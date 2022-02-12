class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            cen = (left + right)//2
            if nums[cen] < target:
                left = cen + 1
            elif nums[cen] > target:
                right = cen - 1
            else:
                return cen
        return -1

