"""

1262. Greatest Sum Divisible by Three
Medium
1.5K
36
Shopee
company
Bloomberg
company
Apple
Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.



Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).


Constraints:

1 <= nums.length <= 4 * 104
1 <= nums[i] <= 104
Accepted
43.8K
Submissions
86.2K
Acceptance Rate
50.9%
Seen this question in a real interview before?
1/4
Yes


"""
from itertools import combinations

# First attempt


def all_subsequences(nums: list):
    max_seen = 0
    for r in range(1, len(nums) + 1):
        for c in combinations(nums, r):
            curr_sum = sum(c)
            if curr_sum % 3 == 0:
                max_seen = max(sum(c), max_seen)

    return max_seen

# 4 lines DP solution


def maxSumDivThree(nums: list):
    dp = [0, float('-inf'), float('-inf')]
    for n in nums:
        dp = [max(dp[i], dp[(3 - n % 3 + i) % 3]+n) for i in range(3)]
    return dp[0]


print(all_subsequences([3, 6, 5, 1, 8]))
