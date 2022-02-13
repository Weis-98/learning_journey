class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(candidates, target):
            ans = []
            if target < candidates[0]:
                return []
            else:
                for i in range(len(candidates)):
                    if candidates[i] > target:
                        break
                    elif candidates[i] == target:
                        ans.append([target])
                    else:
                        items = backtrack(candidates, target - candidates[i])
                        if items:
                            for lines in items:
                                if candidates[i] <= lines[0]:
                                    ans.append([candidates[i]] + lines)
            return ans

        return backtrack(candidates,target)



