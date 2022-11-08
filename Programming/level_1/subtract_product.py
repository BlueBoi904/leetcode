"""

1281. Subtract the Product and Sum of Digits of an Integer
Easy
1.7K
203
company
Google
company
Uber
company
Facebook
Given an integer number n, return the difference between the product of its digits and the sum of its digits.


Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21


Constraints:

1 <= n <= 10^5
Accepted
311.5K
Submissions
359.3K
Acceptance Rate
86.7%
Seen this question in a real interview before?
1/4
Yes
No
Related Topics

"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        main_sum = 0

        res = map(int, str(n))
        for digit in res:
            product *= digit
            main_sum += digit

        return product - main_sum
