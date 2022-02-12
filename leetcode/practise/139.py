class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        matrix = {
            0: True
        }
        for i in range(1, len(s)+1):
            flag = False
            for j in range(i):
                if matrix[j] and s[j : i] in wordDict:
                    flag = True
                    break
            matrix[i] = flag
        return matrix[len(s)]

