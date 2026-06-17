class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []
        l = 0
        for r in range(len(nums)):
            while len(queue) > 0 and nums[r] > nums[queue[-1]]:
                queue.pop()
            
            queue.append(r)

            if r - l + 1 == k:
                res.append(nums[queue[0]])
                if queue[0] == l:
                    queue.popleft()

                l += 1
         
        return res