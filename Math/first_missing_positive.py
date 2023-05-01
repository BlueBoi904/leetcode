"""

41. First Missing Positive
Hard
13.8K
1.6K
company
Microsoft
company
Amazon
company
Google
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

"""

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums_set, i = set(nums), 1
        while i in nums_set:
            i += 1
        return i