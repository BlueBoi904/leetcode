class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor != 0:
            ans = int(dividend/divisor)

            if ans >= (2**31):
                return (2**31)-1
            else:
                return ans
