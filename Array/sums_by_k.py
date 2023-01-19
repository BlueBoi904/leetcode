"""

Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:

Input: nums = [5], k = 9
Output: 0

"""

from collections import defaultdict


def subarrays_div_by_k(nums: list, k: int):
    valid_sub_count = 0
    subs = []

    for i in range(len(nums) + 1):
        for j in range(i + 1, len(nums) + 1):
            subs.append(nums[i:j])

    for sub in subs:
        if sum(sub) % k == 0:
            valid_sub_count += 1
    return valid_sub_count


def sub_div_by_k(nums: list, k: int):
    cur, count, d = 0, 0, defaultdict(int, {0: 1})
    for i in nums:
        cur += i
        rem = cur % k
        count += d[rem]
        d[rem] += 1
    return count


print(subarrays_div_by_k([4, 5, 0, -2, -3, 1], 5))
print(subarrays_div_by_k([5], 9))
