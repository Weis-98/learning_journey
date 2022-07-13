from typing import List

class Solution1:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        fmax = nums[0]
        fmin = nums[0]
        ans = nums[0]

        for num in nums[1:]:
            fmax, fmin = max(fmax * num, fmin * num, num), min(fmax * num, fmin * num, num)
            if fmax > ans:
                ans = fmax
        return ans
