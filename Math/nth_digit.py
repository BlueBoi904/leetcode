"""

400. Nth Digit
Medium
877
1.8K
company
Apple
company
Google
company
Adobe
Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].

 

Example 1:

Input: n = 3
Output: 3
Example 2:

Input: n = 11
Output: 0
Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
 

Constraints:

1 <= n <= 231 - 1
Accepted
85K
Submissions
248.7K
Acceptance Rate
34.2%

"""

class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1
        cnt = 9
        st = 1
        while cnt*digit < n:
            n -= cnt*digit
            digit += 1
            cnt *= 10
            st *= 10

        st += (n- 1)/digit
        st = str(st)
        return int(st[(n-1)%digit])