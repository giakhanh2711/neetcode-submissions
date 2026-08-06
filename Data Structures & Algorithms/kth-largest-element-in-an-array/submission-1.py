class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        priority_queue = []
        for i in range(len(nums) -  k + 1):
            heapq.heappush(priority_queue, -nums[i])
        for i in range(len(nums) - k + 1, len(nums)):
            heapq.heappush(priority_queue, -nums[i])
            heapq.heappop(priority_queue)
        
        return -priority_queue[0]