class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, curSet, curSum):
            for j in range(i, len(candidates)):
                if i < j < len(candidates) and candidates[j - 1] == candidates[j]:
                    continue
                if curSum + candidates[j] <= target:
                    curSet.append(candidates[j])
                    if curSum + candidates[j] == target:
                        res.append(curSet.copy())
                        curSet.pop()
                        return
                    backtrack(j + 1, curSet, curSum + candidates[j])
                    curSet.pop()
                else:
                    return
        
        backtrack(0, [], 0)
        return res