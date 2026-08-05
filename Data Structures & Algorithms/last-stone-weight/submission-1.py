class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stones = []
        for s in stones:
            heapq.heappush(new_stones, -s) 
        while len(new_stones) >= 2:
            x = heapq.heappop(new_stones)
            y = heapq.heappop(new_stones)
            if x != y:
                heapq.heappush(new_stones, -abs(x - y))
        
        return -new_stones[0] if new_stones else 0