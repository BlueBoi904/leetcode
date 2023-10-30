"""

1067. Digit Count in Range
Hard
88
24
company
Amazon
Given a single-digit integer d and two integers low and high, return the number of times that d occurs as a digit in all integers in the inclusive range [low, high].



Example 1:

Input: d = 1, low = 1, high = 13
Output: 6
Explanation: The digit d = 1 occurs 6 times in 1, 10, 11, 12, 13.
Note that the digit d = 1 occurs twice in the number 11.
Example 2:

Input: d = 3, low = 100, high = 250
Output: 35
Explanation: The digit d = 3 occurs 35 times in 103,113,123,130,131,...,238,239,243.


Constraints:

0 <= d <= 9
1 <= low <= high <= 2 * 108

"""

# First attempt
def digits_count(d: int, low: int, high: int) -> int:
    # Count in range low to high
    d_count = 0
    for i in range(low, high + 1):
        digits = [int(x) for x in str(i)]
        for digit in digits:
            if digit == d:
                d_count += 1

    return d_count

# Optimized solution


print(digits_count(1,1,13))

print(digits_count(3,100,250))