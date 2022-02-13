class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        L, R = -1, -1
        left = 0
        right = n - 1
        # search Left barrier
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                if left == right:
                    L = right
                    break
                right = mid

        left = 0
        right = n - 1
        # search Right barrier
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                if left + 1 == right:
                    if nums[right] != target:
                        R = left
                    else:
                        R = right
                    break
                if left == right:
                    R = left
                    break
                left = mid
        return [L, R]

