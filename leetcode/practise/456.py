class Solution:
    def find132pattern(self, nums) -> bool:
        M_min = pow(10, 9)
        M_max = -pow(10, 9)
        abs_list = [[M_min, M_max]]
        for i in range(len(nums)):
            if nums[i] < abs_list[-1][0]:
                abs_list.append([nums[i], M_max])
            for li in range(len(abs_list)):
                if nums[i] > abs_list[li][1]:
                    abs_list[li][1] = nums[i]
                if abs_list[li][0] < nums[i] < abs_list[li][1]:
                    return True
        return False