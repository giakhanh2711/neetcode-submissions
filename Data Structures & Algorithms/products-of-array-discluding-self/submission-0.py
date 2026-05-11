class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        pre = 1
        for i in range(len(nums)):
            result.append(pre)
            pre *= nums[i]
        
        suf = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suf
            suf *= nums[i]
        
        return result