from queue import Queue


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        lens = 0
        hashmap = {}

        if len(s) == 1:
            return 1

        for right, c in enumerate(s):
            if c in hashmap.keys() and hashmap[c] >= left:
                lens = max(lens, right - left)
                left = hashmap[c] + 1

            hashmap[c] = right

        lens = max(lens, len(s) - left)

        return lens

