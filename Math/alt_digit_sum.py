class Solution:
    def alternateDigitSum(self, n: int) -> int:
        flag = True
        digits = [int(digit) for digit in str(n)]
        for i, digit in enumerate(digits):
            if not flag:
                digits[i] = digits[i] * -1
            flag = not flag

        return sum(digits)
