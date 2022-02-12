class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for item in strs:
            dic = [0] * 26
            for char in item:
                dic[ord(char) - ord('a')] += 1

            if tuple(dic) not in mp.keys():
                mp.update({tuple(dic) : [item]})
            else:
                mp[tuple(dic)].append(item)
        return list(mp.values())

