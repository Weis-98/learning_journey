class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    left = mid
                else:
                    right = mid
            else:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                else:
                    right = mid - 1

        if left == right:
            return nums[left]




