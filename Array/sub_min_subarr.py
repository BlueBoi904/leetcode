"""

    907. Sum of Subarray Minimums
Medium
5.4K
365
company
Amazon
company
Microsoft
company
Dunzo
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.



Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444


Constraints:

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104
Accepted
129.4K
Submissions
361.2K
Acceptance Rate
35.8%

"""

# First attempt -> Accepted -> Time Limit Exceeded


def sumSubarrayMins(arr: list):
    # Create a hash table to store the sub arrays
    parent_arr = []
    total = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            # Append each sub arr to our parent_arr arr
            parent_arr.append(arr[i: j])

    # Traverse through the parent_arr arr and find min for each item in the ar
    for mini_arr in parent_arr:
        curr_min = float('inf')
        for num in mini_arr:
            curr_min = min(curr_min, num)

        total += curr_min

    return total


# Second attempt

def sum_subarray_mins(arr: list):
    mod = (10 ** 9) + 7
    stack = []
    dp = [0] * len(arr)
    for i, n in enumerate(arr):
        while stack and arr[stack[-1]] >= n:
            stack.pop()

        if stack:
            dp[i] = dp[stack[-1]] + (n * (i - stack[-1]))

        else:
            dp[i] = n * (i + 1)

        stack.append(i)

    return sum(dp) % mod


sumSubarrayMins(arr=[3, 1, 2, 4])  # =>
