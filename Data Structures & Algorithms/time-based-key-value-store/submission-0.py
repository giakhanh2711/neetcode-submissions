class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        
        data = self.data[key]
        l, r = 0, len(data) - 1
        while l <= r:
            mid = (l + r) // 2
            if data[mid][1] == timestamp:
                return data[mid][0]
            if data[mid][1] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        
        if r < 0 and data[l][1] > timestamp:
            return ""
        if l == len(data) or data[l][1] > timestamp:
            return data[r][0]
        return data[l][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)