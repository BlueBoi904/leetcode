"""

258. Add Digits
Easy
3.1K
1.7K
company
Amazon
company
Apple
company
Bloomberg
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 

Constraints:

0 <= num <= 231 - 1
 

Follow up: Could you do it without any loop/recursion in O(1) runtime?

"""

# First atttempt solution, passes!


def add_digits(num: int) -> int:
    # Create a base case
    if len(str(num)) == 1:
        return num
    curr_sum = 0
    for digit in str(num):
        curr_sum += int(digit)
    return add_digits(curr_sum)


print(add_digits(38))
print(add_digits(0))

# Faster solution


def addDigits(num: int):
    return 1 + (num - 1) % 9 if num else 0
