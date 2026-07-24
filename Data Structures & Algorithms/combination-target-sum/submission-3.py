class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, curSet, curSum):
            if i >= len(nums) or curSum > target:
                return
            
            if curSum == target:
                res.append(curSet.copy())
                return
            
            curSet.append(nums[i])
            curSum += nums[i]
            backtrack(i, curSet, curSum)
            curSet.pop()
            curSum -= nums[i]
            backtrack(i + 1, curSet, curSum)
        
        backtrack(0, [], 0)
        return res

