class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0

        while left < right:
            temp = (right - left) * min(height[right], height[left])
            if res < temp:
                res = temp
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return res

