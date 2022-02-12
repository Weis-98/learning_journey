class Solution:
    #def permutation(self, s: str) -> List[str]:
    def permutation(self, s: str):
        """
        f1: O(n^2)暴力枚举，按照A^8_8的方式构造。第i个位置从剩下的(n-i-1)个元素中选一个，再用set去重。略
        f2: O(n*logn)确认各个元素数量，根据元素表构造树"""
        "f2"
        chars = set(list(s))
        chdict = {}
        for i in chars:
            chdict[i] = s.count(i)
        tree = {0: {"": chdict}}

        for i in range(len(s)):
            tree[i+1] = {}
            for key, v in tree[i].items():
                for c, count in v.items():
                    tempv = v.copy()
                    if tempv[c] == 0:
                        continue
                    else:
                        tempv[c] -= 1
                        tree[i + 1].update({key+c: tempv})
        restree = tree[len(s)]
        res = []
        for key, _ in restree.items():
            res.append(key)
        return res