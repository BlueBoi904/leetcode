"""

905. Sort Array By Parity
Easy
4.2K
134
company
Amazon
company
Facebook
company
Microsoft
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.



Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000

"""


class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        # Move even ints to beginning of arr, and odd to the back
        res = []

        def is_even(num):
            return num % 2 == 0
        for num in nums:
            if is_even(num):
                res.append(num)

        for num in nums:
            if not is_even(num):
                res.append(num)

        return res


def sort_arr_by_parity(nums: list[int]):
    even = []
    odd = []
    for i in nums:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even+odd
