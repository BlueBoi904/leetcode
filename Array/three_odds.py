"""

Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.


Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.


Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000

"""


def threeConsecutiveOdds(arr):
    def is_odd(num):
        return num % 2 != 0

    for i in range(0, len(arr)):
        p1, p2, p3 = i, i + 1, i + 2
        if p3 < len(arr) and is_odd(arr[p1]) and is_odd(arr[p2]) and is_odd(arr[p3]):
            return True

    return False
