"""

1588. Sum of All Odd Length Subarrays
Easy
2.7K
206
company
Adobe
company
Google
company
Facebook
Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.



Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
Example 2:

Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
Example 3:

Input: arr = [10,11,12]
Output: 66

"""


def sumOddLengthSubarrays(arr: list):
    odd_arr_total = 0

    for i in range(len(arr) + 1):
        for j in range(i):
            if len(arr[j: i]) % 2 != 0:
                odd_arr_total += sum(arr[j: i])
    
    return odd_arr_total


sumOddLengthSubarrays([1, 4, 2, 5, 3])  # => 58
