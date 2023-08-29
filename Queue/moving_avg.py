from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.nums = deque()
        self.s = 0

    def next(self, val: int) -> float:
        self.s += val
        self.nums.append(val)
        if len(self.nums) > self.size:
            self.s -= self.nums.popleft()
        return self.s / len(self.nums)