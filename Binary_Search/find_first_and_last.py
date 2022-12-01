"""

34. Find First and Last Position of Element in Sorted Array
Medium
14.9K
363
company
Amazon
company
Facebook
company
Bloomberg
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
Accepted
1.4M
Submissions
3.3M
Acceptance Rate
41.6%
Seen this question in a real interview before?
1/4
Yes
No
Similar Questions
Related Topics


"""


def search_range(nums: list, target: int):
    def bsLeft(nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

    def bsRight(nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return right

    left = bsLeft(nums, target)
    right = bsRight(nums, target)
    return [left, right] if left <= right else [-1, -1]


print(search_range([5, 7, 7, 8, 8, 10], 8))  # => [3,4]
print(search_range([5, 7, 7, 8, 8, 10], 6))  # => [-1,-1]
print(search_range([], 0))  # => [-1,-1]
