class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        for n in nums:
            heapq.heappush(self.nums, n)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
