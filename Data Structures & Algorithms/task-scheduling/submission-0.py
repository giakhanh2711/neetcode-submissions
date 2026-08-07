class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_fre = defaultdict(int)
        for t in tasks:
            count_fre[t] += 1
        max_heap = [-val for val in count_fre.values()]
        heapq.heapify(max_heap)
        
        time = 0
        queue = deque()
        while max_heap or queue:
            time += 1
            if max_heap:
                task_to_do = heapq.heappop(max_heap)
                if task_to_do + 1 < 0:
                    queue.append((task_to_do + 1, time + n))
            
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        
        return time
