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
        