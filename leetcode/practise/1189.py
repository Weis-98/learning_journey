from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = "balloon"
        stat = Counter()
        for c in text:
            if c in target:
                stat[c] += 1

        stat['l'] //= 2
        stat['o'] //= 2

        if len(stat) == 5:
            return int(min(stat.values()))
        else:
            return 0

