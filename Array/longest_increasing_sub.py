"""

674. Longest Continuous Increasing Subsequence
Easy
2K
168
company
Facebook
company
Google
company
Microsoft
Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.
Example 2:

Input: nums = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.

"""


def longest_continuous_sub(nums: list):
    # Keep track of the longest sub_sequence that is continuous increasing

    longest_sub = 1
    nums.append('#')
    curr = 1
    for idx, val in enumerate(nums):
        if nums[idx + 1] == '#':
            break
        if nums[idx] < nums[idx + 1]:
            curr += 1
        else:
            curr = 1
        longest_sub = max(longest_sub, curr)
        # Return the longest sub

    return longest_sub


print(longest_continuous_sub([1, 3, 5, 4, 7]))
print(longest_continuous_sub([2, 2, 2, 2, 2]))
