class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for a in range(n):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            target = - nums[a]
            right = n - 1
            for left in range(a + 1, n):
                if left > a + 1 and nums[left] == nums[left - 1]:
                    continue
                while right > left and nums[left] + nums[right] > target:
                    right -= 1
                if left == right:
                    break
                if nums[left] + nums[right] == target:
                    res.append([nums[a], nums[left], nums[right]])

        return res

