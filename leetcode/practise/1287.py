class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]

        gap = len(arr) // 4 + 1

        for i in range(0, len(arr), gap):
            left = max(0, i - gap)
            right = i
            while (left < right):
                mid = (right + left) // 2
                if arr[mid] < arr[i]:
                    left = mid + 1
                elif arr[mid] == arr[i]:
                    right = mid
            detec_l = right

            left = i
            right = min(len(arr) - 1, i + gap)
            while (left < right):
                mid = (right + left) // 2 + 1
                if arr[mid] == arr[i]:
                    left = mid
                elif arr[mid] > arr[i]:
                    right = mid - 1
            detec_r = left

            if detec_r - detec_l + 1 >= gap:
                return arr[i]

        return -1

