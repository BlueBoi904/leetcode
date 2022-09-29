"""

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
 
Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""


def maxSubArray(nums):
    max_sum, cur_sum = float('-inf'), 0
    for n in nums:
        cur_sum = max(cur_sum + n, n)
        max_sum = max(max_sum, cur_sum)
    return max_sum


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
