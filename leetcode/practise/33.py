class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:   # <= is the KEY! if [0, 1] query = 0 satisify the < < , then the right answer 0 will be removed.
                    left = mid + 1
                else:
                    right = mid - 1
            else:# nums[mid] > nums[right] means that nums[left] <= nums[mid]
                if nums[left] <= target < nums[mid]:    # <= is the KEY! if [0, 1] query = 1 satisify the < < , then the right answer 1 will be removed.
                    right = mid - 1
                else:
                    left = mid + 1
        return - 1

