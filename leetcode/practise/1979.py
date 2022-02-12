class Solution:
    def findGCD(self, nums: List[int]) -> int:
        Max, Min = max(nums), min(nums)

        for i in range(Min, 0, -1):
            if Max % i == 0 and Min % i == 0:
                return i

