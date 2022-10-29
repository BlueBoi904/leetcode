""""

523. Continuous Subarray Sum
Medium
4K
390
company
Facebook
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

 

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1

"""

# First attempt works but too slow


def checkSubarraySum(nums, k):
    curr_window_sum = 0
    # Check all sub arrays in the arr

    # If sub arr sum % 6 == 0 => return True
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            curr_sum = sum(nums[i:j + 1])
            if curr_sum % k == 0:
                return True

    # Return false, no sub arr found
    return False

#

    def checkSubarraySum(nums: list[int], k: int) -> bool:
        lookup = {0: -1}
        curr_sum = 0

        for i, n in enumerate(nums):
            if k != 0:
                curr_sum = (curr_sum + n) % k
            else:
                curr_sum += n
            if curr_sum not in lookup:
                lookup[curr_sum] = i
            else:
                if i - lookup[curr_sum] >= 2:
                    return True
        return False


checkSubarraySum([23, 2, 6, 4, 7])  # => True
