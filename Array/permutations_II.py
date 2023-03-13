"""

47. Permutations II
Medium
7.2K
127
company
Amazon
company
LinkedIn
company
Google
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
Accepted
762.7K
Submissions
1.3M
Acceptance Rate
57.2%

    """


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = list(set(itertools.permutations(nums)))
        result = []
        for i in range(len(res)):
            result.append([])
            for num in res[i]:
                result[i].append(num)

        return result
