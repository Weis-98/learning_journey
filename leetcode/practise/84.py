class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        F1: naive, fix the left side, run the right side
        :param heights:
        :return:
        """
        n = len(heights)
        max_len = n
        ans = 0
        for i in range(n):# 起始点
            max_h = heights[i]
            for j in range(i, n):
                max_h = min(max_h, heights[j])
                ans = max(ans, max_h * (j - i + 1))
        return ans

    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        F2: naive, fix the height, run the wide
        :param heights:
        :return:
        """
        n = len(heights)
        ans = 0
        for mid in range(n):  # 高
            mid_h = heights[mid]
            left, right = mid, mid
            while left - 1 >= 0 and heights[left - 1] >= mid_h:
                left -= 1
            while right < n - 1 and heights[right + 1] >= mid_h:
                right += 1
            ans = max(ans, mid_h * (right - left + 1))

        return ans

    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        F3: single stack
        :param heights:
        :return:
        """
        n = len(heights)
        if n == 0:
            return 0
        left = [0] * n
        right = [0] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            else:
                left[i] = -1
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            else:
                right[i] = n
            stack.append(i)

        vol = [0] * n
        for i in range(n):
            vol[i] = (right[i] - left[i] - 1) * heights[i]

        return max(vol)

    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        F4: single stack + track
        :param heights:
        :return:
        """
        n = len(heights)
        if n == 0:
            return 0
        left = [0] * n
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                right[stack[-1]] = i
                stack.pop()
            if stack:
                left[i] = stack[-1]
            else:
                left[i] = -1
            stack.append(i)

        vol = [0] * n
        for i in range(n):
            vol[i] = (right[i] - left[i] - 1) * heights[i]

        return max(vol)