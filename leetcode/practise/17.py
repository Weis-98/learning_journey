class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num2c = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        n = len(digits)
        if n == 0:
            return res
        ptr = [0] * n
        sup = [len(num2c[i]) - 1 for i in digits]
        temp = ''
        for i in range(n):
            temp += num2c[digits[i]][ptr[i]]
        res.append(temp)
        p = n - 1
        while p >= 0:
            if ptr[p] < sup[p]:
                ptr[p] += 1
                for k in range(p + 1, n):
                    ptr[k] = 0
                temp = ''
                for i in range(n):
                    temp += num2c[digits[i]][ptr[i]]
                res.append(temp)
                p = n - 1
                continue
            if ptr[p] == sup[p]:
                p -= 1

        return res

