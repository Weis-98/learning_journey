class Solution:
    def isUgly(self, n: int) -> bool:
        if not n:
            return False
        factor = [2, 3, 5]
        for i in factor:
            while not n % i:
                n //= i
        if n == 1:
            return True
        return False
