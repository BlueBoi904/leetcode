"""

2177. Find Three Consecutive Integers That Sum to a Given Number
Medium
549
175
FPT
Given an integer num, return three consecutive integers (as a sorted array) that sum to num. If num cannot be expressed as the sum of three consecutive integers, return an empty array.

 

Example 1:

Input: num = 33
Output: [10,11,12]
Explanation: 33 can be expressed as 10 + 11 + 12 = 33.
10, 11, 12 are 3 consecutive integers, so we return [10, 11, 12].
Example 2:

Input: num = 4
Output: []
Explanation: There is no way to express 4 as the sum of 3 consecutive integers.
 

Constraints:

0 <= num <= 1015
Accepted
34.3K
Submissions
53.7K
Acceptance Rate


"""

# First attempt, brute force


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        res = []

        for i in range(num):
            l, m, r = i - 1, i, i + 1
            if l + m + r == num:
                return [l, m, r]

        return res


# Second attempt, optimized solution


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 == 0:
            num //= 3
            return [num - 1, num, num + 1]
        return []
