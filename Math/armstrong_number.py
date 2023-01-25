"""

1134. Armstrong Number
Easy
177
19
company
Amazon
Given an integer n, return true if and only if it is an Armstrong number.

The k-digit number n is an Armstrong number if and only if the kth power of each digit sums to n.

 

Example 1:

Input: n = 153
Output: true
Explanation: 153 is a 3-digit number, and 153 = 13 + 53 + 33.
Example 2:

Input: n = 123
Output: false
Explanation: 123 is a 3-digit number, and 123 != 13 + 23 + 33 = 36.

"""


def isArmstrong(n: int) -> bool:
    digits = [int(digit) for digit in str(n)]

    k = len(digits)

    digits_k = [pow(digit, k) for digit in digits]
    return sum(digits_k) == n


print(isArmstrong(153))
print(isArmstrong(123))
