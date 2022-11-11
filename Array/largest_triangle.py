"""

976. Largest Perimeter Triangle
Easy
2.4K
337
company
Apple
company
Tesla
company
Adobe

Given an integer array nums,

return the largest perimeter of a triangle with a non-zero area,

formed from three of these lengths.
If it is impossible to form any triangle of a non-zero area, return 0.



Example 1:

Input: nums = [2,1,2]
Output: 5
Example 2:

Input: nums = [1,2,1]
Output: 0


Constraints:

3 <= nums.length <= 104
1 <= nums[i] <= 106
Accepted
177.3K
Submissions
324.8K
Acceptance Rate
54.6%
Seen this question in a real interview before?
1/4
Yes
No
Similar Questions
Related Topics

"""


def largestPerimeter(nums) -> int:
    # Iterate through the arr of nums. Find the highest perimeter number that have an area == 0 n1 * n2 * n3 = 0
    # triange in-equality a+b > c
    # sum of 2 smallest > largest
    nums.sort(reverse=True)
    a, b, c = inf, inf, inf
    for n in nums:
        a, b, c = n, a, b
        if a + b > c:
            return a+b+c
    return 0


largestPerimeter([2, 1, 2])  # => 5
