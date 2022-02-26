class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


    def singleNumber(self, nums: List[int]) -> int:
        """
        hashmap : 进表再出表
        :param nums:
        :return:
        """
        s = set()
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        return s.pop()