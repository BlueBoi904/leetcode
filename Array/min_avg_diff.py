"""

2256. Minimum Average Difference
Medium
1.2K
144
company
Amazon
company
Facebook
You are given a 0-indexed integer array nums of length n.

The average difference of the index i is the absolute difference between the average of the first i + 1 elements of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.

Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.

Note:

The absolute difference of two numbers is the absolute value of their difference.
The average of n elements is the sum of the n elements divided (integer division) by n.
The average of 0 elements is considered to be 0.

"""


def minimumAverageDifference(nums: list):
    n = len(nums)
    ans = -1
    min_avg_diff = math.inf
    curr_prefix_sum = 0

    # Get total sum of array.
    total_sum = 0
    for index in range(n):
        total_sum += nums[index]

    for index in range(n):
        curr_prefix_sum += nums[index]

        # Calculate average of left part of array, index 0 to i.
        left_part_average = curr_prefix_sum
        left_part_average //= (index + 1)

        # Calculate average of right part of array, index i+1 to n-1.
        right_part_average = total_sum - curr_prefix_sum
        # If right part have 0 elements, then we don't divide by 0.
        if index != n - 1:
            right_part_average //= (n - index - 1)

        curr_difference = abs(left_part_average - right_part_average)

        # If current difference of averages is smaller,
        # then current index can be our answer.
        if curr_difference < min_avg_diff:
            min_avg_diff = curr_difference
            ans = index

    return ans


minimumAverageDifference()
minimumAverageDifference()
minimumAverageDifference()
