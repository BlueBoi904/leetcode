"""

693. Binary Number with Alternating Bits
Easy
1.2K
107
company
Yahoo
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

 

Example 1:

Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101
Example 2:

Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.
Example 3:

Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.
 

Constraints:

1 <= n <= 231 - 1
Accepted
111.1K
Submissions
180.4K
Acceptance Rate
61.6%

"""


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_num = bin(n)[2:]
        next_idx = 1
        for curr in range(0, len(bin_num) - 1):
            if bin_num[curr] == bin_num[next_idx]:
                return False
            next_idx += 1

        return True
