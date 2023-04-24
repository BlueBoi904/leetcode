# First attempt

class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        res = []
        def is_sequential(num: int):
            digits = [int(x) for x in str(num)]
            i = len(digits) -1
            while i > 0:
                if digits[i] != digits[i - 1] + 1:
                    return False
                i -= 1
            return True
        

            
        

        
        for i in range(low, high + 1):
            if is_sequential(i):
                res.append(i)
        return res
        

# Optimized solution
from collections import deque
class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        out = []
        queue = deque(range(1,10))
        while queue:
            elem = queue.popleft()
            if low <= elem <= high:
                out.append(elem)
            last = elem % 10
            if last < 9: queue.append(elem*10 + last + 1)
                    
        return out