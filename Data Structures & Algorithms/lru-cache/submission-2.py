class Node:
        def __init__(self, key=0, val=0, prev=None, next=None):
            self.key = key
            self.val = val
            self.prev = prev
            self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.data = {}
        

    def get(self, key: int) -> int:
        if key in self.data and self.data[key]:
            self.update_latest(key)
            return self.data[key].val
        
        return -1
        
    
    def update_latest(self, key):
        node = self.data[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        tmp = self.head.next
        node.next = tmp
        tmp.prev = node
        self.head.next = node
        node.prev = self.head


    def put(self, key: int, value: int) -> None:
        if key in self.data and self.data[key]:
            self.data[key].val = value
            self.update_latest(key)
            return

        if self.count == self.capacity:
            remove = self.tail.prev
            remove.prev.next = self.tail
            self.tail.prev = remove.prev
            self.data[remove.key] = None
            self.count -= 1

        node = Node(key, value)
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node
        self.data[key] = node
        self.count += 1
