# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        bottom = 0
        ceil = n
        while bottom < ceil:
            mid = bottom + (ceil - bottom)//2
            if guess(mid) > 0:
                bottom = mid + 1
            else:
                ceil = mid
        return bottom