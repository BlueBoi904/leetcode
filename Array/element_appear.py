"""

Element Appearing More Than 25% In Sorted Array


Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1

"""

from collections import Counter


def findSpecialInteger(arr):
    num_count = Counter(arr)
    return num_count.most_common(1)[0][0]


findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10])  # => 6
findSpecialInteger([1, 1])  # => 1
