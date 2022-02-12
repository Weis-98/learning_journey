# F1
# class Solution:
#     def search(self, nums, target: int) -> bool:
#         n = len(nums)
#         if n == 1:
#             return nums[0] == target
#         mid = nums[0]
#         for i in range(len(nums) - 1):
#             if nums[i] == target or nums[i + 1] == target:
#                 return True
#             if target < mid:
#                 if nums[i] < nums[i + 1]:
#                     continue
#                 else:
#                     mid = nums[i + 1]
#             else:
#                 if nums[i] < target < nums[i + 1]:
#                     return False


# F2
class Solution:
    def search(self, nums, target: int) -> bool:
        n = len(nums)
        if not nums:
            return False
        if n == 1:
            return nums[0] == target
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return False


s = Solution()
print(s.search([], 1))
print(s.search([1], 1))
print(s.search([2, 5, 6, 0, 0, 1, 2], 0))
print(s.search([2, 5, 6, 0, 0, 1, 2], 3))
print(s.search([1,0,1,1,1], 0))
print(s.search([1,1,1,1,2], 2))
print(s.search([0,1,1,1,2], 0))

