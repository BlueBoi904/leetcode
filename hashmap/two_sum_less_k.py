"""

1099. Two Sum Less Than K
Easy
928
108
company
Amazon
company
Capital One
company
TikTok
Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.



Example 1:

Input: nums = [34,23,1,24,75,33,54,8], k = 60
Output: 58
Explanation: We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: nums = [10,20,30], k = 15
Output: -1
Explanation: In this case it is not possible to get a pair sum less that 15.


Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 1000
1 <= k <= 2000
Accepted
106.1K
Submissions
175K
Acceptance Rate
60.6%
Seen this question in a real interview before?
1/4
Yes
No

"""


def twoSumLessThanK(nums: list[int], k: int):
    max_seen_sum = -1
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] < k:
                max_seen_sum = max(max_seen_sum, nums[i] + nums[j])

    return max_seen_sum


twoSumLessThanK([34, 23, 1, 24, 75, 33, 54, 8], 60)
twoSumLessThanK([10, 20, 30], 15)
