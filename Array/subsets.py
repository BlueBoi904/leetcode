"""

Given an integer array nums of unique elements, return all possible
subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

"""


def subsets(nums):
    # Get all combinations of arr
    output = [[]]

    for num in nums:
        output += [curr + [num] for curr in output]
    return output


subsets([1, 2, 3])  # => [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

subsets([0])  # => [[],[0]]
