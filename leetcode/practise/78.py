class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i):
            ans = []
            if i == 0:
                return [[], [nums[0]]]
            temp = backtrack(i - 1)
            for item in temp:
                ans.append(item)
                ans.append(item + [nums[i]])
            return ans
        return backtrack(len(nums) - 1)

