"""

    540. Single Element in a Sorted Array
Medium
7.1K
117
company
Amazon
company
Adobe
company
Infosys
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.



Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105

    """

# First Try


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for count in counts:
            if counts[count] == 1:
                return count
