class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, curSet):
            if i >= len(nums):
                res.append(curSet.copy())
                return
            
            backtrack(i + 1, curSet)
            curSet.append(nums[i])
            backtrack(i + 1, curSet)
            curSet.pop()
        
        backtrack(0, [])
        return res