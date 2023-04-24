"""

2455. Average Value of Even Numbers That Are Divisible by Three
Easy
236
24
company
IBM
Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.

Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.

 

Example 1:

Input: nums = [1,3,6,10,12,15]
Output: 9
Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.
Example 2:

Input: nums = [1,2,4,7,10]
Output: 0
Explanation: There is no single number that satisfies the requirement, so return 0.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
Accepted
36.4K
Submissions
61.3K
Acceptance Rate
59.3%

"""

class Solution:
    def averageValue(self, nums: list[int]) -> int:
        res = []
        def is_valid_num(number: int):
            return number % 2 == 0 and number % 3 == 0
        for num in nums:
            if is_valid_num(num):
                res.append(num)
        if not res:
            return 0
        avg = sum(res)//len(res)
        return avg