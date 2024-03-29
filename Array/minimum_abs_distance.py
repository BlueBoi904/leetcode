"""

1200. Minimum Absolute Difference
Easy
1.9K
64
company
Paypal
company
Bloomberg
Dell

Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

    a, b are from arr
    a < b
    b - a equals to the minimum absolute difference of any two elements in arr



Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

Example 2:

Input: arr = [1,3,6,10,15]
Output: [[1,3]]

Example 3:

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]



Constraints:

    2 <= arr.length <= 105
    -106 <= arr[i] <= 106



"""

# First attempt, correct but not quite fast enough.


from itertools import pairwise


def minimumAbsDifference(arr: list[int]) -> list[list[int]]:

    res = []

    def find_min_diff():
        min_difference = float('inf')
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                temp_diff = abs(arr[j] - arr[i])
                min_difference = min(temp_diff, min_difference)

        return min_difference

    curr_min = find_min_diff()
    for a in range(len(arr)):
        for b in range(a + 1, len(arr)):
            if abs(arr[b] - arr[a]) == curr_min:
                curr = sorted([arr[a], arr[b]])
                res.append(curr)
    res.sort(key=lambda x: x[0])
    return res

# Faster solution


class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:

        arr.sort()
        ans = []
        mi = float('inf')
        for a, b in pairwise(arr):
            d = b - a
            if d < mi:
                ans = [(a, b)]
                mi = d
            elif d == mi:
                ans.append((a, b))
        return ans


print(minimumAbsDifference([4, 2, 1, 3]))

print(minimumAbsDifference([1, 3, 6, 10, 15]))

print(minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]))
