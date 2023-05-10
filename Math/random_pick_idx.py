# First attempt, correct but too slow

from collections import defaultdict
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        res = [i for i, x in enumerate(self.nums) if x == target]
        return  random.choice(res)

# Optimized solution
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = defaultdict(list)
        for i, n in enumerate(nums):
            self.nums[n].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.nums[target])
        