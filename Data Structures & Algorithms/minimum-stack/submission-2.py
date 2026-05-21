class MinStack:

    def __init__(self):
        self.curMin = [float('inf')]
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.curMin.append(min(val, self.curMin[-1]))
        

    def pop(self) -> None:
        self.curMin.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.curMin[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()