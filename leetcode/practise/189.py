class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        F1 数组拼接（切片）
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0:
            return

        temp = nums[n - k:n]
        nums[:] = temp + nums[0:n - k]
        return


    def rotate(self, nums: List[int], k: int) -> None:
        """
        F2 通过reverse方法
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0:
            return
        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            return
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        return

