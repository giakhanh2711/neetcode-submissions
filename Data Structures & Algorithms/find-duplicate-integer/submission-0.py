class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            count = 0
            for n in nums:
                if low <= n <= mid:
                    count += 1
            if count > mid - low + 1:
                high = mid
            else:
                low = mid + 1
        
        return low