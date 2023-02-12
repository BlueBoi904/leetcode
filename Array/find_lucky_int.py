"""

1394. Find Lucky Integer in an Array
Easy
878
26
company
Apple
company
Microsoft
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.



Example 1:

Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
Example 2:

Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
Example 3:

Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.

"""
from collections import Counter
# First attempt, works well!
def findLucky(arr: list[int]):
    counts = Counter(arr)
    lucky_nums = []

    for count in counts:
        if counts[count] == count:
            lucky_nums.append(count)
        
    if len(lucky_nums): return max(lucky_nums) 

    return -1

print(findLucky([2,2,3,4]))
print(findLucky([1,2,2,3,3,3]))
print(findLucky([2,2,2,3,3]))