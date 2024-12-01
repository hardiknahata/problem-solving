from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.buffer = deque()

    def next(self, val: int) -> float:
        self.buffer.append(val)
        if len(self.buffer) > self.size:
            self.buffer.popleft()
        return sum(self.buffer)/len(self.buffer)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)