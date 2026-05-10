class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for n, cnt in count.items():
            bucket[cnt].append(n)
        
        res = []
        i = -1
        while k > 0:
            if bucket[i]:
                res.append(bucket[i][-1])
                bucket[i].pop()
                k -= 1
            else:
                i -= 1
        
        return res