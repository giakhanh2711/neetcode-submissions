class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        dct = {x:True for x in nums}
        res = []

        def backtrack(cur_arr, i):
            if i >= len(nums):
                res.append(cur_arr.copy())
                return
            
            for choice in dct:
                if not dct[choice]:
                    continue
                
                dct[choice] = False
                cur_arr[i] = choice
                backtrack(cur_arr, i + 1)
                dct[choice] = True
        
        backtrack([0]*len(nums), 0)
        return res