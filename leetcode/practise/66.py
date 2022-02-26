class Solution:
    def plusOne(self, digits):
        flag = 1
        for i in range(len(digits)-1,-1,-1):
            temp = digits[i]
            if flag:
                temp = temp + 1
                if temp >= 10:
                    temp -= 10
                    flag = 1
                    digits[i] = temp
                else:
                    digits[i] = temp
                    flag = 0
                    break
        if flag == 1:
            digits = [1] + digits
        return digits

    def plusOne(self, digits: List[int]) -> List[int]:
        """
        适度优化
        :param digits:
        :return:
        """
        up = 1
        for end in range(len(digits) - 1, -1, -1):
            if digits[end] == 9:
                digits[end] = 0
            else:
                digits[end] += 1
                return digits
        return [1] + digits