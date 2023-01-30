"""

2427. Number of Common Factors
Easy
325
6
Given two positive integers a and b, return the number of common factors of a and b.

An integer x is a common factor of a and b if x divides both a and b.



Example 1:

Input: a = 12, b = 6
Output: 4
Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.
Example 2:

Input: a = 25, b = 30
Output: 2
Explanation: The common factors of 25 and 30 are 1, 5.


Constraints:

1 <= a, b <= 1000

"""


def common_factors(a: int, b: int):
    n = max(a, b)
    common_factor_count = 0

    for i in range(1, n + 1):
        if a % i == 0 and b % i == 0:
            common_factor_count += 1

    return common_factor_count


print(common_factors(12, 6))  # => 4
print(common_factors(25, 30))  # => 4
