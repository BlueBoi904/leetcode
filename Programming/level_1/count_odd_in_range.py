"""

1523. Count Odd Numbers in an Interval Range
Easy
1.2K
82
company
Amazon
company
Adobe
company
Accenture
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
 

Constraints:

0 <= low <= high <= 10^9
Accepted
153.9K
Submissions
332.4K
Acceptance Rate
46.3%
Seen this question in a real interview before?
1/4
Yes
No
Related Topics

"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = int((high - low) / 2)

        def is_even(num: int):
            return num % 2 == 0
        if is_even(low) and is_even(high):
            return res
        else:
            return res + 1
