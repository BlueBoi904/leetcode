"""

1207. Unique Number of Occurrences
Easy
2.2K
51
company
Amazon
company
Adobe
company
Google
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.



Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true


Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
Accepted
177.9K
Submissions
250.5K


"""

from collections import Counter


def uniqueOccurrences(arr: list):
    counts = Counter(arr)
    seen_counts = set()
    for count in counts:
        curr = counts[count]
        if curr in seen_counts:
            return False
        seen_counts.add(curr)

    return True


print(uniqueOccurrences([1, 2, 2, 1, 1, 3]))
print(uniqueOccurrences([1, 2]))
print(uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
