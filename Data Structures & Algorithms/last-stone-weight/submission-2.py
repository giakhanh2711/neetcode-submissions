class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_stone = max(stones)
        bucket = [0] * (max_stone + 1)
        for s in stones:
            bucket[s] += 1
        
        first = max_stone
        second = first - 1
        while first:
            if bucket[first] % 2 == 0:
                first -= 1
                continue
            
            second = min(first - 1, second)
            
            while second and bucket[second] == 0:
                second -= 1
            
            if second == 0:
                return first
            
            bucket[second] -= 1
            bucket[first - second] += 1
            first -= 1
        
        return 0