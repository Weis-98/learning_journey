class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_dict = {}
        lens = -1
        for idx, c in enumerate(s):
            if c not in char_dict.keys():
                char_dict.update({c: idx})
            else:
                if idx - char_dict[c] - 1 > lens:
                    lens = idx - char_dict[c] - 1
        return lens