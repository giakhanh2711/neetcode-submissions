class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        v = right
        
        while left <= right:
            mid = (left + right) // 2
            eat_time = 0
            for p in piles:
                eat_time += math.ceil(p / mid)
            if eat_time <= h:
                v = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return v