class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(n):  # inner function to make code simpler
            if n in cache:
                return cache[n]
            else:
                cache[n] = climb(n-1) + climb(n-2)
                return cache[n]
        cache = {1: 1, 2: 2}  # base cases
        return climb(n)