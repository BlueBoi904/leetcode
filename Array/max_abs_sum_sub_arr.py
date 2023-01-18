"""

You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.


Example 1:

Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
Example 2:

Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.

"""

# Running solution, time limit exceeded


def max_absolute_sum(nums: list):
    # store all the sublists
    curr_max = float("-inf")
    sub_list = [[]]

    # first loop
    for i in range(len(nums) + 1):

        # second loop
        for j in range(i + 1, len(nums) + 1):

            # slice the sublist
            sub = nums[i:j]
            sub_list.append(sub)

    for sub in sub_list:
        temp_sum = abs(sum(sub))
        curr_max = max(curr_max, temp_sum)
    return curr_max


def maxAbsoluteSum(nums: list):
    mi = 0
    ma = 0
    s = 0
    for i in nums:
        s += i
        mi = min(mi, s)
        ma = max(ma, s)
    return ma-mi


print(max_absolute_sum([1, -3, 2, 3, -4]))
print(max_absolute_sum([2, -5, 1, -4, 3, -2]))
