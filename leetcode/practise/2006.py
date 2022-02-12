from collections import Counter


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        num2idx = Counter()
        res = 0
        for i, num in enumerate(nums):
            num2idx[num] += 1
            res += num2idx[num + k] + num2idx[num - k]

        return res

