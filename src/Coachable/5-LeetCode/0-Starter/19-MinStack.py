class MinStack:

    def __init__(self):
        self.arr = []  # (curr, min so far)

    def push(self, val: int) -> None:
        if not self.arr:
            self.arr.append((val, val))
            return
        last, last_min = self.arr[-1]
        self.arr.append((val, min(val, last_min)))

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.arr[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
