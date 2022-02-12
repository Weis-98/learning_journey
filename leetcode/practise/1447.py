class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(a, b):
            while a:
                a, b = b % a, a
            return b

        res = []
        for i in range(2, n + 1):
            for j in range(i):
                if gcd(j, i) == 1:
                    res.append('{}/{}'.format(j, i))

        return res

