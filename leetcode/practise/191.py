class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)
        return str(bin(n)).count('1')