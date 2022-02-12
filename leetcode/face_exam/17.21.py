# 给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6

# F1
# class Solution:
#     def trap(self, height) -> int:
#         water = 0
#         L_threshold = 0
#         R_threshold = 0
#         l = 0
#         r = len(height) - 1
#         while r >= l:
#             if L_threshold <= R_threshold:
#                 if height[l] < L_threshold:
#                     water += L_threshold - height[l]
#                 else:
#                     L_threshold = height[l]
#                 l += 1
#             else:
#                 if height[r] < R_threshold:
#                     water += R_threshold - height[r]
#                 else:
#                     R_threshold = height[r]
#                 r -= 1
#         return water

# F2 单调栈
class Solution:
    def trap(self, height) -> int:
        nums = []
        maxh = 0
        water = 0
        for i, h in enumerate(height):
            while nums and h > height[nums[-1]]:
                top = nums.pop()
                if not nums:
                    break
                left = nums[-1]
                width = i - left - 1
                lenth = min(height[left], height[i]) - height[top]
                water += width * lenth
            nums.append(i)
        return water


s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
