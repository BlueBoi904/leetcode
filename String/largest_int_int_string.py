"""

1903. Largest Odd Number in String
Easy
715
57
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
Example 2:

Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".
Example 3:

Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.


Constraints:

1 <= num.length <= 105
num only consists of digits and does not contain any leading zeros.

"""

# First attempt solution, passes but too slow.


class Solution:
    def largestOddNumber(self, num: str) -> str:
        B = []

        def is_odd(my_num: int):
            return my_num % 2 != 0

        # first loop
        for i in range(len(num) + 1):
            # second loop
            for j in range(i + 1, len(num) + 1):
                # slice the subarray
                sub = int(num[i:j])
                B.append(sub)
        B.sort(reverse=True)
        for item in B:
            if is_odd(item):
                return str(item)
        return ''


def largest_odd_number(num: str):
    last_ind = -1

    # Iterate through all the numbers for finding a odd number that appears on the last.
    for i, j in enumerate(num[::-1]):
        if (int(j) % 2 != 0):
            last_ind = len(num) - i
            break

    # If there is no odd number, return empty string.
    if (last_ind == -1):
        return ""

    # Or return the string upto that index.
    return (num[:last_ind])
