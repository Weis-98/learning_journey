# F1
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# F2
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashdict = {}
        for index, num in enumerate(nums):
            if target - num in hashdict:
                return [hashdict[target - num], index]
            hashdict[num] = index
        return []